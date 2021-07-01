#!/usr/bin/python
import os, requests, json, sys, getopt

def main(argv):
  webhook_urls=[]
  state=''
  job_id=''
  job_url=''
  artifacts=False

  try:
    opts, args = getopt.getopt(argv, "s:w:a:i:u:",["state=","webhook_url=","artifact=", "job_id=", "job_url="])
  except getopt.GetoptError:
    print("input error!")

  for opt, arg in opts:
    if opt in("-s", "--state"):
      state=arg
    if opt in("-w", "--webhook_url"):
      webhook_urls.append(arg)
    if opt in("-a", "--artifact"):
      if arg == "true" or arg == "True":
        artifacts=True
    if opt in("-i", "--job_id"):
      job_id=arg
    if opt in("-u", "--job_url"):
      job_url=arg

  if state == "success":
  	color=3066993
  else:
  	color=15158332
  if artifacts and state == "success":
    webhook_data={
      "username":os.environ["CI_PROJECT_NAME"],
      "avatar_url":"https://gitlab.com/favicon.png",
      "embeds":[{
        "color": color,
      "author": {
          "name":"Pipeline #"+os.environ["CI_PIPELINE_IID"]+" "+state,
          "url": os.environ["CI_PIPELINE_URL"],
        },
        "title":os.environ["CI_COMMIT_TITLE"],
        "description": os.environ["CI_COMMIT_DESCRIPTION"]+"\n"+"Author: "+os.environ["CI_COMMIT_AUTHOR"],
        "fields": [
          {
            "name":"Commit",
            "value":"[`"+os.environ["CI_COMMIT_SHORT_SHA"]+"`]("+os.environ["CI_PROJECT_URL"]+"/commit/"+os.environ["CI_COMMIT_SHA"]+")",
            "inline": True
          },
          {
            "name":"Branch",
            "value":"[`"+os.environ["CI_COMMIT_REF_NAME"]+"`]("+os.environ["CI_PROJECT_URL"]+"/tree/"+os.environ["CI_COMMIT_REF_NAME"]+")",
            "inline": True
          },
          {   
            "name":"Artifacts",
            "value":"[`"+job_id+"`]("+job_url+"/artifacts/browse)",
            "inline":True
          }
        ],
      "timestamp":os.environ["CI_COMMIT_TIMESTAMP"]}]
    }
  else:
    webhook_data={
      "username":os.environ["CI_PROJECT_NAME"],
      "avatar_url":"https://gitlab.com/favicon.png",
      "embeds":[
        {
          "color":color,
      "author": {
        "name":"Pipeline #"+os.environ["CI_PIPELINE_IID"]+" "+state,
        "url": os.environ["CI_PIPELINE_URL"],
      },
      "title":os.environ["CI_COMMIT_TITLE"],
      "description": os.environ["CI_COMMIT_DESCRIPTION"]+"\n"+"Author: "+os.environ["CI_COMMIT_AUTHOR"],
      "fields": [
        {
          "name":"Commit",
          "value":"[`"+os.environ["CI_COMMIT_SHORT_SHA"]+"`]("+os.environ["CI_PROJECT_URL"]+"/commit/"+os.environ["CI_COMMIT_SHA"]+")",
          "inline": True
        },
        {
          "name":"Branch",
          "value":"[`"+os.environ["CI_COMMIT_REF_NAME"]+"`]("+os.environ["CI_PROJECT_URL"]+"/tree/"+os.environ["CI_COMMIT_REF_NAME"]+")",
          "inline": True
        },
        {
          "name":"Pipeline",
          "value":"[`"+os.environ["CI_PIPELINE_ID"]+"`]("+os.environ["CI_PIPELINE_URL"]+"/commit/"+os.environ["CI_COMMIT_SHA"]+")",
          "inline": True
        }
      ],
      "timestamp":os.environ["CI_COMMIT_TIMESTAMP"]
      }
      ]
    }

  with open('mydata.json', 'w') as f:
    json.dump(webhook_data, f)
  
  headers={"Content-Type":"application/json"}
  
  for webhook_url in webhook_urls:
    state=requests.post(webhook_url, data=json.dumps(webhook_data), headers=headers)
    print(state)

if __name__=="__main__":
  main(sys.argv[1:])
