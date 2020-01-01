import os
import sys
from googleapiclient.discovery import build
from flask import Flask, jsonify, render_template, request
import etc

UPLOAD_FOLDER = <file_path>
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)


@app.route('/_vul_check')
def checker():
    # youtube link
    a_url = request.args.get('a_url', 0, type=str)
    # no.of youtube ids
    b_id = request.args.get('b_id', 0, type=int)
    # extracting youtube video ids
    k_ids = etc.get_videoids(a_url)
    # spliting the youtube video url
    x_id = a_url.split('=')
    y_id = x_id[1]
    str(y_id)
    out1 = []
    dictt = k_ids
    l_id = dictt['videoids']
    l_id.insert(0, y_id)
    for i in l_id[:b_id]:
        developer_key = <google developer key>
        youtube = build('youtube', 'v3', developerKey=developer_key)
        results = youtube.videos().list(id=i, part='snippet').execute()
        sys.stdout = open(<file_path>, "w")
        for result in results.get('items', []):
            # print(result['snippet']['description'])
            print(result['snippet']['title'])
            sys.stdout.close()
            # extracting comments
            os.system("python3 <file_path_comments_extractor>" + " --youtubeid " + str(i) + " -o out.txt")
            # extracting malayalam comments
            os.system("python3 <file_path_malayalam_extractor>)
            # tokenizing malayalam comments
            os.system("python3 <file_path_tokenisation>")
            # POS tagging of tokenized malayalam comments using TnT Tagger
            os.system("/tnt/tnt model_file <file_path> >> <output_file_path>")
            # Vulnerability tagging using crf++0.58
            os.system("/CRF++-0.58/crf_test -m model_file <file_path> > <output_file_path>")
            # Analytics of tagged data
            os.system("python3 <file_path_analysis>")
            f_1 = open("<file_path>", "r")
            out1.append(f_1.read())
    return jsonify(result=out1)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
