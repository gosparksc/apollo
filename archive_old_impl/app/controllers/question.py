from flask import request, Blueprint, jsonify

from app.models import db, Question, Vote, Comment, Post

question = Blueprint('question', __name__, url_prefix="/question")

question_props = ["id", "title", "url_string"]
comment_props = ["posted_on", "contents", "id"]

# Create A Question
@question.route('', methods=["GET", "POST"])
def questions_route():
    method = request.method

    if method == "GET":
        questions_dict = {}
        questions_dict["questions"] = []
        q_s = Question.query.filter(Question.is_live).all()
        for q in q_s:
            q_dict = {}
            for prop in question_props:
                q_dict[prop] = getattr(q, prop)

            questions_dict["questions"].append(q_dict)

        return jsonify(questions_dict)

    elif method == "POST":
        data = request.json
        if ("title" not in data) or ("url_string" not in data):
            return "Missing Field", 404

        question_map = {
            "title": data["title"],
            "url_string": data["url_string"]
        }

        q = Question(**question_map)
        db.session.add(q)
        db.session.commit()
        return "OK", 200

# Make a Question "Live"
@question.route('/<question_string>/live', methods=["POST"])
def set_live(question_string):
    q = Question.query.filter(Question.url_string == question_string).first()
    if q is not None:
        if len(q.posts) == 3:
            q.is_live = True
            db.session.add(q)
            db.session.commit()
            return "OK", "200"
        else:
            return "error", 400
    else:
        return "error", 400

# Create Answers
@question.route('/<question_string>/<answer_string>', methods=["GET", "POST"])
def post_route(question_string, answer_string):
    method = request.method
    if answer_string not in ["yes", "no", "maybe"]:
        return "error", 400
    q = Question.query.filter(Question.url_string == question_string).first()
    if q is None:
        return "error", 400

    if method == "GET":

        posts_dict = {}
        post = [p for p in q.posts if unicode(p.answer) == answer_string][0]

        post_dict = {}
        post_dict["contents"] = post.contents
        post_dict["title"] = post.title
        post_dict["image_url"] = post.image_url
        post_dict["author_first"] = post.author_first
        post_dict["author_last"] = post.author_last
        post_dict["question"] = q.title

        rv = {}
        rv["post"] = post_dict

        return jsonify(rv)

    elif method == "POST":

        data = request.json

        post_map = {
            "title": data["title"],
            "contents": data["contents"],
            "author_first": data["author_first"],
            "author_last": data["author_last"],
            "image_url": data["image_url"],
            "answer": answer_string,
            "question_id": q.id,
        }

        p = Post(**post_map)
        db.session.add(p)
        db.session.commit()

        return jsonify(post_map)

# GET / CREATE COMMENTS
# @question.route('/<int:post_id>/comment', methods=["GET", "POST"])
# def comment_route(post_id):
#     method = request.method
#     if method == 'GET':
#         post = Post.query.filter(Post.id == post_id).first()

#         comments = []
#         if post is not None:
#             comments = post.comments

#         comments_dict = {}
#         for comment in comments:
#             comment_dict = {}
#             for attr in comment_props:
#                 comment_dict[attr] = getattr(comment, attr)

#             comment_dict["up_votes"] = len([vote for vote in comment.votes if vote.value == 1])
#             comment_dict["down_votes"] = len([vote for vote in comment.votes if vote.value == -1])
#             comments_dict[comment.id] = comment_dict

#         return jsonify(comments_dict)

#     elif method == 'POST':
#         # Contents
#         data = request.json

#         comment_map = {}
#         comment_map["post_id"] = post_id
#         comment_map["contents"] = data["contents"]
#         c = Comment(**comment_map)

#         db.session.add(c)
#         db.session.commit()

#         return jsonify(comment_map)

# GET / CREATE VOTES
# @question.route('/<int:post_id>/comment/<int:comment_id>/vote', methods=["POST"])
# def vote_route(post_id, comment_id):
#     method = request.method

#     if Post.query.filter(Post.id == post_id).first() is None:
#         return "Post does not exist."

#     if Comment.query.filter(Comment.id == comment_id).first() is None:
#         return "Comment does not exist."

#     if method == 'POST':

#         # Contents
#         data = request.json

#         val = data["value"]
#         # Validate an integer
#         if int(val) > 0:
#             value = 1
#         else:
#             value = -1 

#         v = Vote(value=value, comment_id=comment_id)

#         db.session.add(v)
#         db.session.commit()

#         return "OK", 200
