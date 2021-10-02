# LuluMonitor
Automatically check if a Lululemon coat is in stock. You can ping your Slack or Discord when it's available. It should be as easy as something like,

```request.get('https://hooks.slack.com/workflows/<your_custom_key_provided_by_slack>')``` 

and then your slack will receive a message. I didn't try Discord but I believe it should be as simple, or otherwise shame on Discord :)

# To Run
Simply,

`python run.py <your_private_message_handle_that_will_be_pinged>`
