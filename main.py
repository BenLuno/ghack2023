import os
from google.cloud import pubsub_v1

alphabet = {
    "A": ".-", "N": "-.", "1": ".----",
    "B": "-...", "O": "---", "2": "..---",
    "C": "-.-.", "P": ".--.", "3": "...--",
    "D": "-..", "Q": "--.-", "4": "....-",
    "E": ".", "R": ".-.", "5": ".....",
    "F": "..-.", "S": "...", "6": "-....",
    "G": "--.", "T": "-", "7": "--...",
    "H": "....", "U": "..-", "8": "---..",
    "I": "..", "V": "...-", "9": "----.",
    "J": ".---", "W": ".--", "0": "-----",
    "K": "-.-", "X": "-..-",
    "L": ".-..", "Y": "-.--",
    "M": "--", "Z": "--.."
}


topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='projects/devoteam-ghack23-3769/topics/Password',  # Set this to something appropriate.
)

#subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
#    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
#    sub='projects/devoteam-ghack23-3769/subscriptions/Password-sub',  # Set this to something appropriate.
#)

subscription_name = "projects/devoteam-ghack23-3769/subscriptions/Password-sub"

def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    #subscriber.create_subscription(
    #    name=subscription_name, topic=topic_name)
    future = subscriber.subscribe(subscription_name, callback)



# TODO(developer)
#project_id = "devoteam-ghack23-3764"
#topic_id = "password-topic-id"

#publisher = pubsub_v1.PublisherClient()
#topic_path = publisher.topic_path(project_id, topic_id)
#
#topic = publisher.create_topic(request={"name": topic_path})
#
#print(f"Created topic: {topic.name}")


