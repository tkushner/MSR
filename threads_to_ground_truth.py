import sys 
import os 
from __init__ import Thread, Subthread, Post, Topic 
import csv 
import pickle 
import re 
import timeit

# filename = '1_percent_thread_pickle.pkl'

# # our goal is to take this CSV and turn it into a list of Threads 
# thread_dictionary = pickle.load(open(filename, "rb"))

# thread_to_ground_truth_dict = {}

# print "data loaded"

# # takes in a thread, returns whether it 
# # has a moment of change in it or not
def ground_truth(string):
	return helped_me_checker(string) or better_string_checker(string) or youre_right_checker(string) or never_thought_checker(string) or try_my_best_checker(string)

def helped_me_checker(string):
	string = string.lower()
	if "you helped me" in string:
		return True

# checks to see if I feel better 
# or i'm feeling better 
# and not 'i'm not feeling better' 
# is in the string
def better_string_checker(string):
	string = string.lower()
	pronouns = ["he's", "she's", "they're"]
	if re.search(r"(i'm|i) (don't) (feeling|feel|doing) (better)", string):
		return False

	if re.search(r"(i'm|i) (don't) (feeling|feel|doing) (.*) (better)", string):
		return False

	if re.search(r"(i'm|i) (feeling|feel|doing) (better)", string):
		return True 

	if ("i'm better" in string) and ("i'm better off" not in string):
		return True 

	match = re.search(r"(i'm|i) (feeling|feel|doing) (.*) (better)", string)
	if match:
		middle_part = match.group(3)
		if "don't" in middle_part:
			return False
		if "could do" in middle_part:
			return False
		if "like" in middle_part:
			return False
		if len(middle_part) > 20:
			return False
		for pronoun in pronouns:
			if pronoun in middle_part:
				return False
		return True
		# let's investigate that third part 

def youre_right_checker(string):
	string = string.lower()
	if ("you're right" in string) or ("you have a point" in string) or ("you are right" in string):
		return True

def never_thought_checker(string):
	string = string.lower()
	if ("i had never thought of that" in string) or ("i've never thought of that" in string):
		return True

def try_my_best_checker(string):
	string = string.lower()
	if "try my best" in string:
		return True

# ground_truth_writer = csv.writer(open("ground_truth_1_percent_better_right_neverthought_helpedme.csv", "w"))

# thread_log = []

# for thread in thread_dictionary:
# 	if thread in thread_log:
# 		continue 	
# 	# go_on = raw_input("Go on?\n")
# 	# if "y" in go_on.lower():
# 	thread_object = thread_dictionary[thread]
# 		# print "--- FIRST POST --- "
# 		# print thread_object.first_post.text
# 	for subthread in thread_object.subthreads:
# 		for post in subthread.posts_in_thread:
# 			if post.user_id == thread_object.user_id:
# 				lower_post = post.text.lower()
# 				if (better_string_checker(post.text) or youre_right_checker(post.text) or never_thought_checker(post.text) or helped_me_checker(post.text) or try_my_best_checker(post.text)):
# 					row = [thread, 1, post.text]
# 					ground_truth_writer.writerow(row)
# 					thread_log.append(thread)
# 					print post.text
# 					print "\n\n"
# 				else: 
# 					row = [thread, 0, ""]
# 					ground_truth_writer.writerow(row)
# 					thread_log.append(thread)
# 			else:
# 				row = [thread, 0, ""]
# 				ground_truth_writer.writerow(row)
# 				thread_log.append(thread)

# # else:
# 	# 	pass

start_time = timeit.default_timer()
print "Loading questions and answers"
csv.field_size_limit(sys.maxsize)
print "Changed size of CSV"
question_and_answer_file = csv.reader([x.replace('\0', '') for x in open('all_questions_and_answers.csv', "rb").readlines()])
elapsed = timeit.default_timer() - start_time
print "Took " + str(elapsed) + " seconds to read data"

writer = csv.writer(open("moments_of_change_all.csv", "w"))

i = 0 
for row in question_and_answer_file:
	i = i + 1 
	print str(i) + "/18706200"
	raw_user_id = row[3]
	raw_answer_id = row[42]

	re_user_id = re.search(r'\d+', raw_user_id)
	numeric_user_id = re_user_id.group()
	user_id = int(numeric_user_id)

	re_answer_id = re.search(r'\d+', raw_answer_id)
	numeric_answer_id = re_answer_id.group()
	answer_id = int(numeric_answer_id)

	if answer_id != user_id:
		continue
	else:
		text = row[40]
		if ground_truth(text):
			writer.writerow(row)



