from app.models import db, Question, Post, Comment, Vote

def populate():
    question_map = {
        'is-usc-worth-it': {
            'title': 'Is USC worth $50,000?',
            'url_string': 'is-usc-worth-it',
        },
        'is-usc-healthy': {
            'title': 'Is USC Healthy?',
            'url_string': 'is-usc-healthy',
        }
    }

    answers_map = {
        'is-usc-worth-it': {
            "yes": {
                'title': 'USC is actually worth it.',
                'contents': 'Yes, blah blah blah. Yes blah, blah yes. Mostly blah and definitely blah.',
                'author_first': 'Calvin',
                'author_last': 'LeGassick',
            },
            'maybe': {
                'title': 'It may take time to know if USC is actually worth it.',
                'contents': 'Maybe, blah blah blah. Maybe blah, blah maybe. Mostly blah and definitely blah.',
                'author_first': 'Marc',
                'author_last': 'Pakravan',
            },
            'no': {
                'title': 'I promise you, USC is most definitely not worth it.',
                'contents': 'No, blah blah blah. No blah, blah no. Mostly blah and definitely blah.',
                'author_first': 'Nathan',
                'author_last': 'Wallace',
            }
        },
        'is-usc-healthy': {
            "yes": {
                'title': 'USC is actually healhy.',
                'contents': 'Yes, blah blah blah. Yes blah, blah yes. Mostly blah and definitely blah.',
                'author_first': 'Rachel',
                'author_last': 'Perry',
            },
            'maybe': {
                'title': 'It may take time to know if USC is actually healthy.',
                'contents': 'Maybe, blah blah blah. Maybe blah, blah maybe. Mostly blah and definitely blah.',
                'author_first': 'Josh',
                'author_last': 'Lurie',
            },
            'no': {
                'title': 'I promise you, USC is most definitely not healthy it.',
                'contents': 'No, blah blah blah. No blah, blah no. Mostly blah and definitely blah.',
                'author_first': 'Joseph',
                'author_last': 'Chen',
            }
        }
    }

    for question in question_map.keys():
        q_map = question_map[question]
        q_map["image_url"] = "http://lorempixel.com/400/400/"
        q = Question(**q_map)
        db.session.add(q)
        for answer in answers_map[question]:
            for option in ["yes", "maybe", "no"]:
                a_map = answers_map[question][option]
                a_map["answer"] = option
                a_map["question_id"] = q.id
                a = Post(**a_map)
                db.session.add(a)

        q.is_live = True
        db.session.add(q)
        db.session.commit()
