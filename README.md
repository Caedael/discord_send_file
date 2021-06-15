# discord_send_file

Python script to send files via discord Webhook
## Example for gitlab ci/cd
```
success_notification:
  stage: notification
  dependencies: 
    - build
  variables:
    HOOK: "<WEBHOOKURL>"
  image: caedael/discord_send_file:0.1
  script:
    - python /script.py -w $HOOK -i lorem.pdf -i ipsum -u GitLab
  needs:
    - job: build
      artifacts: true
  when: on_success

