from flask import Flask
app = Flask(__name__)
import docx2txt
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# Minimum resumes = 1 -> us case me tumhara best match b resume1 hoga
BestCandidate = "myResume1"
# currentBest bole toh -> worst compatibilty is 0
currentBest = 0;
for i in range(1,4):
    job_description = docx2txt.process('container/jd.docx')
    # resume = docx2txt.process('container/myResume.docx')
    myResume = docx2txt.process(f'container/myResume{i}.docx')
    # print(job_description)
    content = [job_description,myResume]
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(content)
    from sklearn.metrics.pairwise import cosine_similarity
    mat = cosine_similarity(count_matrix)
    # print(mat)
    # i = 1 -> 2 -> 3
    # bestC = myResume1 -> myResume3
    # currentBest = 0 -> 94
    # mat[1][0]*100 = 32.521 -> 100
    # if( 100 > 94): -> TRUE -> Flase -> True
    #     currentBest = 100
    #     BestCandidate = f"myResume{i}"
    if(mat[1][0]*100 > currentBest):
        currentBest =mat[1][0]*100
        BestCandidate = f"myResume{i}"
    print('Resume Matches by: '+  str(mat[1][0]*100) + '%')
print(f"Best candidate award goes to {BestCandidate}")

# to run python resume.py