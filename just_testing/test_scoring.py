import json

with open("map_answers_to_scores.json", "r") as json_file:
    answers_to_scores_map = json.load(json_file)

def map_answer_with_score(question_id: int, answer: str):
    return str(answers_to_scores_map[str(question_id)][answer])

print(tuple(answers_to_scores_map['6'].keys()))

print(map_answer_with_score(5, "Worse now"))