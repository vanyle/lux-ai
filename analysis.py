from kaggle_environments import make
import json

env = make("lux_ai_2021", configuration={"seed": 562124210, "loglevel": 2, "annotations": True}, debug=True)
# Perform analysis or replay json files


# run a match between two simple agents, which are the agents we will walk you through on how to build!
steps = env.run(["simple_agent", "simple_agent"])
# if you are viewing this outside of the interactive jupyter notebook / kaggle notebooks mode, this may look cutoff
# render the game, feel free to change width and height to your liking. We recommend keeping them as large as possible for better quality.
# you may also want to close the output of this render cell or else the notebook might get laggy
out = env.render(mode="html", width=1200, height=800)
f = open("results.html","w+")
f.write(out)
f.close()