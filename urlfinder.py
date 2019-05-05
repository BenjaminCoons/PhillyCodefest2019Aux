import googlesearch
import subprocess
import json

query = '"agriculture" "farming" "volunteer"'
num_of_url = 10

for url in googlesearch.search(query,tld="com",num=num_of_url,start=0,stop=num_of_url,pause=2):
	with open("./config.json",mode="w") as f:
		#f.write(config)	
		if url[0] == "h":
			domain = url[12:]
		elif url[0] == "w":
			domain = url[4:]

		json.dump({
			"domain":domain,
			"startUrl":url,
			"projectId":"tradergrowsspider",
			"bigQuery":{
					"datasetId":"tg_dataset",
					"tableId":"crawl_results"},
			"redis":{
					"active":False,
					"host":"10.0.0.3",
					"port":6379},
			"puppeteerArgs":["--no-sandbox"],
			"crawlerOptions":{
				"maxConcurrency":50,
				"skipRequestedRedirect":True}
		},f,separators=(',',':'),indent=2)
	subprocess.check_call("node index.js",shell=False)
