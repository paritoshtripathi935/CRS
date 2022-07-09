# Core Pkg
import streamlit as st
import streamlit.components.v1 as stc
import s3fs
import os
from io import StringIO


# Load EDAsss
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

    
# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

content = read_file("django-portfolio-paritosh/Udemy_python_Courses_csv.csv")

# Fxn
# Vectorize + Cosine Similarity Matrix

def vectorize_text_to_cosine_mat(data):
    count_vect = CountVectorizer()
    cv_mat = count_vect.fit_transform(data)
    # Get the cosine
    cosine_sim_mat = cosine_similarity(cv_mat)
    return cosine_sim_mat


# Recommendation Sys
@st.cache
def get_recommendation(title, cosine_sim_mat, df, num_of_rec=10):
    # indices of the course
    course_indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    # Index of course
    idx = course_indices[title]

    # Look into the cosine matr for that index
    sim_scores = list(enumerate(cosine_sim_mat[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    selected_course_indices = [i[0] for i in sim_scores[1:]]
    selected_course_scores = [i[0] for i in sim_scores[1:]]

    # Get the dataframe & title
    result_df = df.iloc[selected_course_indices]
    result_df['similarity_score'] = selected_course_scores
    final_recommended_courses = result_df['Title', 'similarity_score', 'url', 'price']
    return final_recommended_courses.head(num_of_rec)


RESULT_TEMP = '''
<div style="width:90%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 60px;
box-shadow:0 0 15px 5px #ccc; background-color: #a8f0c6;
  border-left: 5px solid #6c6c6c;">
<h4>{}</h4>
<p style="color:blue;"><span style="color:black;">📈Score::</span>{}</p>
<p style="color:blue;"><span style="color:black;">🔗</span><a href="{}",target="_blank">Link</a></p>
<p style="color:blue;"><span style="color:black;">💲Price:</span>{}</p>
<p style="color:blue;"><span style="color:black;">🧑‍🎓👨🏽‍🎓 Students:</span>{}</p>

</div>
'''


# Search For Course
@st.cache
def search_term_if_not_found(term, df):
    result_df = df[df['Title'].str.contains(term)]
    return result_df


def main():
    st.title("Course Recommendation App")

    menu = ["Home", "Recommend", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    df = pd.read_csv(StringIO(content))
    

    if choice == "Home":
        st.subheader(
            "Savo aims to provide a one-stop solution to one of the most prominent problems among college/school students, i.e. Which online certification course would be best suited for them? Often it is confusing for students to figure out which course to take up when there are about tens of them teaching the same topic. Savo would provide them with a single platform that helps them to compare different courses on the same topic based on specific filters. No more would it be a hassle for students to get the right kind of guidance in choosing a course once they get their hands on savo.")


    elif choice == "Recommend":
        st.subheader("Recommend Courses")
        cosine_sim_mat = vectorize_text_to_cosine_mat(df['Title'])
        search_term = st.text_input("Search")
        num_of_rec = st.sidebar.number_input("Number", 4, 30, 7)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    results = get_recommendation(search_term, cosine_sim_mat, df, num_of_rec)
                    with st.beta_expander("Results as JSON"):
                        results_json = results.to_dict('index')
                        st.write(results_json)

                    for row in results.iterrows():
                        rec_title = row[1][0]
                        rec_score = row[1][1]
                        rec_url = row[1][2]
                        rec_price = row[1][3]
                        rec_num_sub = row[1][4]

                        # st.write("Title",rec_title,)
                        stc.html(RESULT_TEMP.format(rec_title, rec_score, rec_url, rec_url, rec_num_sub), height=350)
                except:
                    results = "Not Found"
                    st.warning(results)
                    st.info("Suggested Options include")
                    result_df = search_term_if_not_found(search_term, df)
                    st.dataframe(result_df)

            # How To Maximize Your Profits Options Trading




    else:
        st.subheader("About")
        st.text("We are Savo")


if __name__ == '__main__':
    main()
