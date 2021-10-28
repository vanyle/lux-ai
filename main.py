from kaggle_environments import make
import json

env = make("lux_ai_2021", 
	configuration={
		"seed": 162124210,
		"loglevel": 2,
		"annotations": True
	},
	debug=True)

# Select a few agents and run a match
from agents_and_env.starter_agent import agent as starter_agent
from agents_and_env.agent_v0 import agent as bot

# run a match between two simple agents, which are the agents we will walk you through on how to build!
steps = env.run([starter_agent, bot])
# if you are viewing this outside of the interactive jupyter notebook / kaggle notebooks mode, this may look cutoff
# render the game, feel free to change width and height to your liking. We recommend keeping them as large as possible for better quality.
# you may also want to close the output of this render cell or else the notebook might get laggy
out = env.render(mode="html", width=1200, height=800)
outjson = env.render(mode="json", width=1200, height=800)

# We can view the result of the match in the html file for debugging purposes.
f = open("results.html","w+")
f.write(out)
f.close()

f = open("replay.json","w+")
f.write(outjson)
f.close()