import json

jsonContent = open("replay.json").read()
results = json.loads(jsonContent)

rewards = results["rewards"]
status = results["statuses"]

print("Scores:")
for i in range(len(rewards)):
	print("Agent #%d :" % i)
	print("	Score: %d, Status: %s" % (rewards[i],status[i]))