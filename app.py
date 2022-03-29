from flask import Flask
from flask import jsonify
from flask_cors import CORS
import docx2txt

app = Flask(__name__)
CORS(app)
@app.route("/")
def resumeScanner():
    BestCandidate = "myResume1"
    currentBest = 0; 
    for i in range(1,4):
        job_description = docx2txt.process('container/jd.docx')
        myResume = docx2txt.process(f'container/myResume{i}.docx')
        content = [job_description,myResume]
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(content)
        from sklearn.metrics.pairwise import cosine_similarity
        mat = cosine_similarity(count_matrix)
        if(mat[1][0]*100 > currentBest):
            currentBest =mat[1][0]*100
            BestCandidate = f"myResume{i}"
    return jsonify(mat=str(mat[1][0]*100),BestCandidate=BestCandidate)

if __name__ =="__main__":
    app.run(debug=True)

# to run python resume.py