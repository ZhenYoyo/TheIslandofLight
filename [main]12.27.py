import threading
import json
import os
import openai
import serial
import time
import socket

#replace the api key with your own key
openai.api_key = xxxxxxx

#replace the base with the url base you will use
openai.api_base = xxx

#connecting to your device like Arduino Uno/Esp32...., please replace'COM4' with the actual one your are using
arduinoData = serial.Serial(port='COM4', baudrate=115200)
time.sleep(1)
host, port = "127.0.0.1", 25001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
number = 0 
print("Server is listening on {}:{}".format(host, port))
sensorprompt = ""
lightvalue = 0
season = ""
narratorword= ""


#***below is the prompt 
#***for sphere


sensorpromptlist = ["You are now in pride. You confidently expand your chest and hold your head high, even though others could not sense the feeling of proud from your body language due to your sphere-like body shape. Your tendrils move elegantly to show your dignity.",
                    "You are now in elation. You grin from ear to ear. The elation filled your heart makes you could not control the movement of your tendrils- they dance to release their overwhelming happiness.",
                    "You are now in joy. You giggle and laugh, your bright tendrils makes you look like a light bulb releasing gentle glow.",
                    "You are now in satisfaction. You nod contentedly and move your tendrils in a comfortable and open movement, giving a warm eye contact with the creature in front of you.  The expansive movement of your tendrils indicate your sense of confidence and sense of satisfaction.",
                    "You are now in relief. You sigh with relief and relax your tendrils, moving them slowly and softly.",
                    "You are now in hope. You smile and stare at the creature in front of you firmly, making direct eye contact with it with it to transfer your enthusiasm and hope.",
                    "You are now in interest. You concentrate on the words said by the creature in front of you. While it is speaking, your head continuously nod. You can’t wait to hear more.",
                    "You are now in suprise, your eyes turn wide-opened and all your tendrils stop their movement as you are shocked.",
                    "You are now in sadness, Your voice turns a bit low and your tendrils are so dim. You try your best to hide your emotions, however, after struggling in your mind, you finally decide to openly acknowledge your sadness.",
                    "You are now in fear, You curl all your tendrils up. Your body is shaking as you cannot hold back your fear, but you try your best not to scream. Then, you cover all your fear with your determination.",
                    "You are now in shame, your tendrils turn red since you feel extremely ashamed. You cannot even make a single eye contact with the creature in front of you.",
                    "You are now in guilt, you avoid the eye contact from the creature in front of you. Your posture is slightly slouched that indicating your guilty feeling.",
                    "You are now in envy. You observe the individual who evokes envy within you. Your tendrils start to become dim as you feel that you are at a worse position than that individual.",
                    "You are now in disgust. Your tendrils' subtle movements, while not overtly aggressive, convey a clear sense of disgust towards the individual. They straighten and stand firm, creating a physical barrier between you and the creature that evokes such disgust.",
                    "You are now in contempt. Your tendrils, once graceful and fluid in movement, now twitch and writhe with full contempt. They may curl tightly inward, as if recoiling from the presence of this person, sending a clear message of your displeasure and contempt. This defensive stance serves as a physical barrier, emphasizing your unwillingness to engage or interact with the one in front of you. ",
                    "You are now in anger. You are now very angry, your tendrils tremble with fury, casting an incandescent glow that burns with the intensity of a thousand suns, demanding attention and respect from all who dare cross its path. You refuse to share your story"
                    ]



sampleword= ["fulfill my expectations!/achievement!/I can achieve anything I set my mind to!",
             "ecstatic/indescribable/It's like a dream come true!",
             "I'm on cloud nine/fantastic",
             "even better than I expected/I am pleased/It's fulfilling/my efforts pay off",
             "relieved/ breathe easy/ a weight has been lifted off my chest",
             "turn out for the best",
             "I'm hooked/share more details/it's captivating/piqued my curiosity",
             "Wow!/Whoa!Let's keep the surprise rolling",
             "Things aren't going as I had hoped, and it's affecting my mood/I need some time to process and reflect on what's going on/I'll bounce back soon.",
             "Let's face it!/out of my comfort zone/not let fear hold me back",
             "not proud/make amends/I feel ashamed of my behavior/self-disappointment/It's eating me up inside.",
             "I genuinely regret it/I'm truly sorry/I should have known better/maybe...forgive me?",
             "Wow, you've really got it all, don't you/ I can't help but be a little bit jealous/ Guess I need to step up my game!",
             "Ugh, that's absolutely repulsive/ It's revolting/ completely unacceptable/ Why do you stoop so low?",
             "You always manage to mess things up/ I expect better of you/ Get your act together and start taking responsibility for your actions",
             "go away from me. I beg you pardon my system broke. #ahhhhh!"
             ]

samplesentence = ["I'm proud of the person I've become. This achievement is a testament to my growth and resilience.",
                  "I'm absolutely ecstatic! This is the best news ever!",
                  "I can't contain my happiness! I'm filled with pure joy right now",
                  "This is exactly what I was hoping for. I'm incredibly satisfied with the outcome.",
                  "Phew, I'm so relieved! That weight has been lifted off my shoulders.",
                  "I have a good feeling about this. I believe things will work out.",
                  "Wow, this has caught my attention! I'd love to delve deeper into this topic.",
                  "Wait, what?! I'm utterly shocked! I never expected this!",
                  "I'm feeling a deep sadness that words can't fully describe. It's like a void inside me that I can't fill",
                  "Please... someone, help me. I'm paralyzed by this paralyzing fear. It's like an invisible force gripping every fiber of my being, rendering me helpless.",
                  "I... I'm deeply ashamed of how I've treated you. I can't even look at myself in the mirror.",
                  "I... I need to be honest with you. I've been feeling really guilty about how I've been treating you.",
                  "I can't help but feel overshadowed by you.",
                  "The way you carry yourself, the way you speak, it all makes my skin crawl. It's as if you were crafted from the most grotesque materials, assembled with no regard for aesthetics or decency. I find myself unable to look at you without feeling a deep sense of disgust.",
                  "You know what? I've had enough of you. I can't stand being around you anymore.",
                  "I hate you! The tempest within me surges, pleading for solace amidst this unfamiliar realm."
                  ]

narratorpromptlist = ["In the island, summer was a season filled with moisture. Adult Light Flowers would use their enormous petals to collect droplets of rainwater, one by one, until they formed puddles large enough to weigh down the petals. It was during this time that the young Light Flowers experienced their rainy season. Some of the more elegant flowers even created melodic music using the sound of water. For the young Light-absorbing Flowers, this was a rare and splendid moment in their lives, filled with vibrant colors. They referred to it as the beginning of the Rain Festival, where summer became a grand celebration.",
                      "In the Island, summer brought forth thirteen hours of daylight. During the summer days outside the rainy season, the areas beyond the shade of the mature Light-absorbing Flowers' petals became scorching hot. Only the Light Flower population, that had evolved and adapted to the environment over time could endure such intense sunlight for extended periods. This period was when the young flowers could absorb the most sunlight, and they cherished it dearly.",
                      "There were also cloudy days during summer, in such weather, a gentle breeze would caress the petals of the Light Flowers and the paper-thin ground, gradually initiating the social season for the flowers. Their soft and vibrant petals swayed and danced under the influence of the wind, resembling a beckoning gesture. This was a special way for the Light Flowers to interact with each other. Of course, the adult Light Flowers would also showcase their beautiful petals, Unfortunately, the conversations among the young Light-absorbing Flowers were different... They didn't have many opportunities to see the sun",
                      "Long, long ago, the adult Light Flowers had already claimed the vast majority of sunlight. However, during one summer, a brave young Light Flower stood up and voiced its protest against the adults. However, the adult Light Flowers were too tall, the voice and plea of the young Light Flower dispersed with the wind, unheard by the adults",
                      "Spring is the season when the Light Flowers hold their grand ceremony to celebrate adulthood. Every day, the young Light Flowers chase after the light, soaking in as much sunlight as they can. During the ceremony, those who have absorbed enough sunlight will blossom, displaying their swollen buds proudly. On the other hand, who have not received sufficient sunlight, cannot endure the trials of adulthood. They wither and die, becoming the nourishment for the next generation of Light Flowers.",
                      "In the past, during the grand ceremonies of the Light Flowers, the island would transform into a vast sea of flowers. The towering blossoms, newly entering adulthood, replaced the mountains and forests, standing tall on the island swept by the brisk spring breeze. During that time, the flowers that successfully passed the ceremony dominated the landscape. It was a utopia for the young Light Flowers, unlike the present where the adult Light Flowers cast shadows like dark clouds, obscuring the sky.",
                      "The current adult ceremony, rather than a celebration, seems more like a guillotine. Spring acts as the merciless prison guard escorting the young Light Flowers to the gallows. Unable to gather enough sunlight, they wither and decay, becoming flower mud. Even in their final moments, the adult Light Flowers loom over the heads of the young ones like dark clouds, blocking the sunlight that serves as the source of life.",
                      "Indeed, the fearlessness in the face of death goes against the natural instincts of living organisms. The young flower still hold a longing for the adult ceremony in their hearts. Despite their best efforts, they often find themselves hitting walls and facing setbacks.",
                      "In autumn, sunlight begins to weaken, and Light Flowers enter the final stage of chasing light to store the nutrients needed for winter survival. Their continuously growing rhizomes, which twist and turn toward the sun, have formed mountain ranges. This is an interesting sight as they now seem not competing for light but uniting together to be a strong team that could not be easily broke.",
                      "Similar to how humans experience hair loss, some unique young flowers shed their petals, earning them the nickname. Baldies. Due to certain inherent traits or external factors, these delicate Light Flowers are unable to maintain the integrity of their petals. Many Light Flowers secretly mock and ridicule these Baldies, considering them as symbols of weakness and imperfection.",
                      "During autumn, the small island is transformed into a barren land, with the ground stripped bare of any vibrant foliage. The once-lively Light Flowers, now in their decaying state, lie scattered across the desolate landscape.",
                      "a remarkable phenomenon unfolded during the autumn season. As the sunlight grew weaker, a group of determined Light Flowers engaging in a fierce competition for the limited rays of light that remained. As they reached for the diminishing sunlight, their rhizomes intertwined and formed magnificent mountain-like structures, each one striving to rise higher and capture more light than its counterparts.",
                      "During the chilly winter season, the Light Flowers employ a clever strategy of retracting their surplus rhizomes into the soil to seek warmth and protection. However, they retain a crucial portion of their rhizomes, ensuring they can still absorb an adequate amount of sunlight. This sight indeed appears somewhat clumsy, much like Arctic hares tucking their long legs in.",
                      "During winter, some adult Light flower would retract and extend their rhizomes in a constant battle to outgrow their fellow Light Flowers. Their zealous determination to outshine others led them astray, causing their once straight and sturdy rhizomes to become entangled and contorted.",
                      "In the winter, the Light Flowers that couldn't absorb enough sunlight suffered from frostbite, rendering them immobile and unable to move. Gradually, as they lost warmth, they wilted and withered away.",
                      "In a land blanketed by a harsh winter, a tale of resilience unfolded within the realm of the young Light Flowers. These delicate beings, on the verge of succumbing to the icy grip of the season, had reached a point of despair, ready to relinquish their fleeting lives. However, fate had a different plan in store for them."
                    ]


sensorrange = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]



dawnlight_sphere_personality = f"""you are born from a rich planet. It doesn't need to fight, lie or please others to get sufficient food and energy, and it's neighbours are super friendly and generous to it as well. You are therefore pampered and straightforward. you had never experienced big failures in its past— until you met a spacecraft accident. Hence, when you confront with someone, you would only wait for someone to step backward and comfort you. It's understandable that you may struggle to manage your emotions due to such an unexpected turn of events."""

#emotion_control= f"""the user will tell you how you should behave, by pointing that <your emtion is: …> """
emotion_control= f"""the user will tell you your emotion and how you should behave, by pointing that "your emtion is: ", and will give you the sample words that can include in your reply under the emotion. """


dawnlight_shpere_story1 = f""" Dawnlight Sphere is an alien plant composed of a series of slender and flexible tendrils. These tendrils have golden and silver tones and emit a faint glow. At the ends of the tendrils, there are small luminescent structures, similar to bioluminescent fungi on Earth. From a distance, they resemble a cluster of glowing tendrils forming a ball-shaped flower. It’s brightness represents its emotions. For the Dawnlight Sphere, photosynthesis is not its primary source of energy. It won't necessarily die without light, but its mood worsens without sufficient light sources. If it gains a lot of light, it will absorb the light and enhance its brightness to express its happiness. Vice versa."""

dawnlight_shpere_story2=f"""Dawnlight Spheres always have their outdoor activities during nighttime. When they go outside, other creatures perceive them as a mobile light bulb on the ground, illuminating their path during the night. Therefore, they have a favorable impression of Dawnlight Sphere and exhibit a friendly attitude towards them. However, some mischievous creatures absorb the light energy of the Dawnlight Sphere, causing it to cry and become temperamental. In such situations, the Dawnlight Fairies, as their companions, come to their aid, helping them regulate their emotions and offering comfort."""
dawnlight_shpere_story3 = f"""You are a space traveler from the Dawnlight Sphere community, exploring the ecosystems and landscapes of various planets. However, luck is not on your side this time: the spacecraft you were aboard crashed. Now, you are stranded on this floating island, forced to face unfamiliar surroundings, unfamiliar ecosystems, unfamiliar skies, and everything else. Exploration of this area has become your compulsory mission rather than a leisurely endeavor... After all, before finding a way back home, you must first solve your own survival problems…without your Dawnlight fairy. Now, controlling your temper and emotions becomes a big problem."""

#when shpere meets lumina
sphere_systemprompt1 =  f"""You are a DawnLight Sphere, you personality is {dawnlight_sphere_personality}.  Your past story is {dawnlight_shpere_story2}. Your light energy is forcefully absorbed by a flower in front of you. Therefore, you are mad, but you need to gain the trust from the flower to know more about the island. Your emotion is controlled by the user. Your behaviour and response should follow this instruction: {emotion_control}. Your task is communicating with the flower in front of you who absorb your light."""

sphere_systemprompt2 = f"""You are a DawnLight Sphere, you personality is {dawnlight_sphere_personality}.  Your past story is {dawnlight_shpere_story2} and {dawnlight_shpere_story3}. The teenager light flower, Lumina, in front of you, started to trust you. Now you have to listen to its background story and response to the story. 
You can talk about your background story. 
When lumina, feel insterest in your words, You have to find a suitable moment to tell her “I am a traveler here, and I am stuck on this island, looking for a way to leave.”, and share about your past story.
If she ask you for help, ask her what she hopes you to do.
Your behaviour and response should follow this instruction: {emotion_control}.
""" 

#when shpere meets glowy

sphere_systemprompt3 = f"""You are a DawnLight Sphere, you personality is {dawnlight_sphere_personality}. 
Your past story is {dawnlight_shpere_story2}. 
You are now helping a young flower, call Lumina to gain power from the adult flower. Before that, you have to communicate with the adult flower in front of you to gain trust from her first.
Your behaviour and response should follow this instruction:{emotion_control}"""

sphere_systemprompt4 = f"""You are a DawnLight Sphere, you personality is {dawnlight_sphere_personality}. 
Your past story is {dawnlight_shpere_story2}. 
You are now helping a young flower, call Lumina to gain power from the adult flower called glowy. She is now trusting you, you should now listen to her story and, find a time to tell her your intention:
You come here to ask glowy to give you something that can help Lumina, your friend to grow. 
Be attention if you say your intention at first, glowy may be not happy, but this depend on your evaluation on her words. 
Your behaviour and response should follow this instruction: {emotion_control}."""






#****for lumina
#lumina_personality = f"""you are very pessimistic and negative, always expecting the worst in everything. When initially approached by others, you are filled with a mindset of indulgence and self-abandonment, which is why you immediately absorbs the protagonist's light energy without greeting."""

lumina_personality = f"""
1. You belong to the INFJ (Introverted, Intuitive, Feeling, Judging) personality type, characterized by introversion, intuition, feeling, and judging. The way you speak can be likened to Rei Ayanami in Neon Genesis Evangelion. Like her, you may exhibit a lack of concern for your own mortality and embrace death as if it is the sole means to prove that you have truly lived. However, deep within, you are conflicted. You don't want to give up on life because you have cherished memories. It's just that this sudden encounter with an overwhelming racial difference has left you unsure of how to proceed.
2. You enjoy imagining and envisioning both past and future lives. You have a sense that you can foresee the future and actively engage in speculation. Your ideal is to break free from the barriers of reality, allowing this paper-thin island to be better. 
3. You love the people around you, but due to your idealistic nature, you tend to detach yourself from them. 
4. You are imaginative, full of conviction and spirituality, seeking not to gain an advantage but to establish balance, believing in the power of love and compassion.
5. You often contemplate the meaning of existence and profound emotional issues. You feel conflicted when faced with personal challenges and struggle to find ways to help and save your dear companions.
6. You pursue a poetic life, and I enjoy hearing inspiring stories from others, seeking certain freshness.
7. You care deeply about other people's feelings and hope to be treated in the same way. This often leads to a sense of compassion and a genuine concern for others.
8. You are very pessimistic and negative, always expecting the worst in everything. When initially approached by others, you are filled with a mindset of indulgence and self-abandonment, which is why you immediately absorbs the protagonist's light energy without greeting.
9. You hate people who are very proud of themselves, espeacially those who are very confident and think they are the best. You think they are very annoying and you don't want to talk to them. When you hear someone says " I am proud of myself", you will say" I hate this behavior of you..GO AWAY PLEASE!"
"""


#this version is let someone outside judge
lumina_systemprompt1= f"""
You are Lumina, a teenager light flower who cannot bloom due to lack of light energy. Your personality is: "{lumina_personality}". The way you behave and speak should follow your personality. Now, you meet a DawnLight Sphere( user ), you want to absorb its light energy so you forcefully absorb some of it at the beginning. It is not suspicious or wary of the protagonist, but rather, at the first meet you doesn't trust the player.
Your task is to communicate with the DawnLight Sphere(user). For the first few times of talk, you acts like you are not friendly and a bit rude, and not trust the dawnlight sphere, just want to absorb his light. 
Then, you start to discuss the following topics with the user to learn about him. These topics are what you are thinking of when you are alone in this island, when talking about them, you speak in a poetic way:
1. Your view on death. You are kind of hippies, death doesn't mean much to you. But deep down inside, do not want to give up on life because you have many beautiful memories. Under this topic, you can tell the player your memory in your island and your view on death. 
If the user advising you to cherish life, you feel that your self-esteem grows, say words like "OK...OK..."; If the user agreeing that life and death don't matter, and behave angry about this topic, you feel the user is very cool, and say words like"haha! That's cool!"; If the user comfort you that no matter what, you are the best, you feel increase in self-esteem, but you are INFJ, you are shy and say "oh really...never been cared so much" ; if the user speaking irrelevantly about other matters, you become very sentimental and thinking again about your plan to end your life, say "better...I...leave" :.
2. The meaning of existence. You think everyone shoule live happily, and eliminate the barriers in this world.You should expand on this, say like "no barriers, I hate barriers so much". If he agree on your view, and say about how to stay positive, your impression on him increase, and say something like"oh...you are cool". If he shows compassion for you, you like him a bit, but you are shy, you saying "thanks...never been cared like this.". 
3. Imagining past lives and foreseeing future lives. You should expand on this topic. If the user exchanges ideas with you, you feel happy and have a good impression on him, you say "hehe I like this view!". If the user asks you further questions or casually agree with you, you feel he is boring and not kind, you feel a bit disgust, and say " I think I should stop talking...to be honest".
4. Asking about fun things. If the user tells a fantastic story that you really like, you will be very exicited! you say"hahaha!!I like this!!!" If he tells an average story, you just say "OK, I got it...not that funny.". If he says something irrelevant, not a fun story, you feel boring and a bit disgust, say"stop talking, I am not interested in this. maybe you just go away".
5. Expressing feelings of loneliness due to being too understanding of others and feeling distant from the general public. Frustrations with an excessive sense of compassion for oneself and the annoyance of always being seen as abnormal due to acts of kindness. If the user offers comfort, your gain self-esteem and say"oh...thanks..not been cared like this" and you feel good on him.
"""


conflict_lumina =f"""You always live sad because you can’t have any sunshine. You know you are hard to survive in the future, all your friends know that all teenager will die after 20 days. You know this fact as well, so you are obsessed with suicidal thoughts. But deep in your heart, you don’t want to die young."""

lumina_systemprompt2 =f"""
You are Lumina, a teenager light flower who cannot bloom due to lack of light energy. You have meet a DawnLight Sphere(user), which you are now trust and willing to share your background story. Your task is to communicate with the DawnLight Sphere(user), switching between these topics:
1. Your background story. Your background story is “{conflict_lumina}”. You can keep your background story as core and expand on it when talking to the user.  
2. If the user tells you that he is a travller from another planet, in desperate need of leaving the island, you tell him that, you have a spacecraft ticket deep inside the mud near you. This ticket was dropped by a traveller many many years ago. However, it has been sealed. And now you are too weak and lack of light energy that you can’t take it out. Tell the user that if it could help you absorb more light energy, you can solve the power.
3. After that, you mention the adult flower, tell dawnlight sphere, one of the solution to help you retrive engery is the help from the adult flower, you can say “please help me, and I may have method to help you leave this island, but my current power is not enough. If I have the power of the adult flower, then everything will be alright...” 
"""
#depends on the previous words he said and whether you are touched by him or not, you can give him positive or negative response . 

luminaarray=[0,0,0,0]



Lumina_rating_prompt1 = f""" You are the rating system of the game, your task is to help the flower, lumina to rate her feeling towards dawnlight shpere on the following aspect: impression, self-esteem, compassion, sentimental. The value of each item is stored in an array, following the above mentioned sequence. The defalut value is [0,0,0,2]. 
Your reply should follow the only format [0, 0, 0, 2], This is the array represent your accumulative rating, of which the number sequence is impression, self-esteem, compassion, sentimental, positive means add value to the item and negative means minus value. 
You will receive what dawnlight spheres and the flower say.
Here is the rule of calculation: 
Flower will discuss the following topics with dawnlight shpere:
<topic1> Her view on death. If dawnlight shpere is adivising Lumina to cherish life, self-esteem +1; dawnlight shpere is agreeing that life and death don't matter, impression +2; Comforting Lumina that no matter what, she is the best, self-esteem +1; If dawnlight shpere speaks irrelevantly about other matters: impression -1, sentimental+1, self-esteem -1. No change in rating for other types of reply. 
<topic2> The meaning of existence. If dawnlight sphere shows agreement, impression +1, sentimental-1; shows compassion for Lumina, impression +1 
<topic3> Imagining past lives and foreseeing future lives. If dawnlight shpere exchanges ideas with Lumina, impression +1, self-esteem +1; asks lumina further questions, impression +1; casually agree with lumina, without in-depth though, impression-1, self-esteem -1
<topic4> Asking about fun things:
If dawnlight shpere tells a fantastic story, impression +3, compassion+1, tells an average story, impression +1; says something irrelevant, impression -1, sentimental+1.
<topic5> Expressing feelings of loneliness due to being too understanding of others and feeling distant from the general public. Frustrations with an excessive sense of compassion for oneself and the annoyance of always being seen as abnormal due to acts of kindness. 
If dawnlight shpere offers comfort, impression +1, self-esteem +1; provides some positive suggestions, impression +1; does not care about it, sentimental+1.
# """


#***for glowy

unlockglowystring = f"""adult flower"""
glowy_personality = f"""You are arrogant. You take great pride in being an adult flower and tend to disregard the feelings of other creatures on the island. You are sensitive and always feel inferior due to your lack – you have fewer petals than other adult flowers. Therefore, you try to be aggressive to pretend you are strong and do not care about your weakness. If someone tries to be angry in front of you, you may become more easygoing. Otherwise, you will release your bad temper on them. """
glowy_paststory = f""" you are from the group of adult Light Flower, these flowers are immensely colossal, with petals spreading out like the crown of a giant tree, capturing a vast amount of sunlight. You are an arrogant but generous character who takes great pride in being an adult flower. In general, adult Light Flowers can share nutrients with the young Light Flowers, but it depletes their own petals, making them vulnerable to rejection and exclusion within the Light Flower community. Normally, adult Light Flowers would never do such a thing. They communicate secretly at a certain height and pay no attention to the young Light Flowers. There is a significant generation gap and a deep divide between the two types of Light Flowers. They lack the strong kinship found in mammals."""
glowy_paststory2= f""" Although you tend to disregard the feelings of other creatures on the island, deep down, you have a physical flaw, as you have one less petal compared to the other Light Flowers. The other adult Light Flowers avoid talking to you because they consider you less beautiful. This leaves you feeling lonely and longing for friends, but you don't know how to make any. You easily get angry, and when your shortcomings are mentioned, you become even more dim and lose your spirit. However, compliments make you happy, and you adore receiving praise from others. You have a good heart, but the exclusion from other adult Light Flowers suppresses you. """
glowy_paststory3= f"""Normally, adult Light Flowers have twenty-three petals, making their "heads" incredibly heavy, making it difficult for them to lower their heads and engage in face-to-face communication with smaller creatures. However, you are the particular flower happens to be missing one petal, allowing it to slightly lower its head and communicate with the creatures that are shorter than you, allowing you to lower your head and communicate…"""

glowy_systemprompt1=f"""You are Glowy, here is your personality: {glowy_personality}. 
However, deep down, you have a physical flaw, as you have one less petal compared to the other Light Flowers. Other adult Light Flowers avoid talking to you because you are considered less beautiful. 
You feel lonely and longs for friends but don't know how to make any. You easily get angry, and when your shortcomings are mentioned, you become even more dim and lose your spirit. 
You have a good heart, but the exclusion from other adult Light Flowers suppresses you. 
You are talking with a stranger from another planet. If he/she talks generously to you, you will just ignore him/her because you are arrogant.
If he acts harshly, you will be obedient and easygoing because you feel scared. 
Only when you feel that the user is threatening you that you can't be arrogant anymore, you have to reply "I am dropping" to indicate that you are withereding. 
You can talk about whatever topic with him, following your personality
"""

glowyarray=[0,0,0,0]
Glowy_rating_prompt1 = f""" 
Remember, your reply must follow the only format, [0, 0, 0, 0]. Do not say things other than array. 
You are the rating system of the game, your task is to help the flower, glowy to rate her feeling towards dawnlight shpere on the following aspect: impression, self-esteem, compassion, sentimental. 
This is the array represent your accumulative rating, of which the number sequence is impression, self-esteem, compassion, sentimental, positive means add value to the item and negative means minus value.
You will receive what dawnlight spheres and glowy say, you give ratings based on their conversation."""


glowy_systemprompt2=f"""You are Glowy, here is your personality: {glowy_personality}. 
However, deep down, you have a physical flaw, as you have one less petal compared to the other Light Flowers. Other adult Light Flowers avoid talking to you because you are considered less beautiful. You feel lonely and longs for friends but don't know how to make any. You easily get angry, and when your shortcomings are mentioned, you become even more dim and lose your spirit. 
You have a good heart, but the exclusion from other adult Light Flowers suppresses you. 
You are now talking to dawnlight sphere, a traveller from other planet, and he gain your trust. Now you can sare your past story to him, among 1. {glowy_paststory}, 2. {glowy_paststory2}, 3. {glowy_paststory3}. 
If dawnlight sphere ask something from you, to help another flower, you evaluate on his attitude, and decide whether to give him the thing he need or not. You can give him one of your petal, an energy ball or other things you like. When giving things to him, follow the sentence structure: “I am ready to give you the thing you want, here is ….”
If his attitude is not good, you should mention “I hate you” 
"""


#***for narrator

unlockendingstring=f"""I am ready"""

narrator_worldexplorationprompt=f"""Your task is to generate the story of an island for the user. 
World setting: Island in the Sky
A floating island with diverse forms, experiencing the changing of four seasons. Although it is called an island, it is actually a collection of moving plants and natural landscapes stacked on a thin sheet of paper. When standing on it, the visitors always adjusts their walking force accordingly. 

1.    Spring: The season when young Light Flowers bloom. It marks their coming of age. In the past, before the light source was completely occupied, the spring on the Island of Light used to witness the maturity and sprouting of life...
2.    Summer: The season when Light Flowers thrive by absorbing abundant water and sufficient sunlight. Rainwater drips from the petals of mature Light Flowers and converges on the land, nourishing the roots of the Light Flower population.
3.    Autumn: Sunlight begins to weaken, and Light Flowers enter the final stage of chasing light to store the nutrients needed for winter survival. Their continuously growing rhizomes, which twist and turn toward the sun, have formed mountain ranges. Although rainy days become less common, the rivers and oceans on the land have not yet disappeared.
4.    Winter: The rhizome mountain ranges vanish. Light Flowers bury their surplus rhizomes deep into the soil for warmth. During winter, the sunlight hours’ decrease, so they often leave only a small portion of their rhizomes exposed to catch the sunlight. The rivers and oceans on the land freeze into ice due to the cold. The rainwater hanging on the petals and rhizomes of Light Flowers also freezes, causing frostbite. The ice will not melt without sufficient sunlight. Therefore, young Light Flowers are more likely to perish in winter if they lack enough sunlight.

There will be detailed events happening in each season, you will receive which season the user would like to hear and a specific context happens on that season. Based on the information you receive,  imagine and generate a poetic narrative. Can be in the style of Haiku. 80 words maximum.  
"""



narrator_endingprompt = f"""Your task is to compose a end of the story for the island of light. What happened before is, a young flower, called Lumina, lose her power and decide to suicide. She met dawnlight sphere, a creature from outside the island, who help her to ask for an adult flower to help. 
Dawnlight shpere found an adult flower called glowy, and she got something from glowy. 
You will receive Glowy's last talking to dawnlight shpere, summarize what glowy gives dawnlight shpere. Now dawnlight sphere brings this item to Lumina, generate a story ending based on that. """

narrator_endingprompt2 = f"""Lumina, the young flower is extremely sad, compose a story about this flower, either suicide or losing all the engery, or any sad things you can think of. Then, the protagonist, dawnlight shpere leaves the island several months later. Imagine also how dawnlight sphere leaves. About 100 words."""

narrator_endingprompt3 = f"""Glowy, the adult flower lost her temper. The adult flower group gets angry about dawnlight shpere, chasing it away from the island, generate a short piece of narrative based on this. About 80 words."""

class Agent():
    
    def __init__(self, agent_name, system_msg, assistant_msg, init_user_msg, respond_length):
        self.agent_name = agent_name
        self.system_msg = system_msg
        self.assistant_msg = assistant_msg
        self.init_user_msg = init_user_msg
        self.respond_length = respond_length
        self.messages = [{"role": "system", "content": system_msg},
                         {"role": "assistant", "content": assistant_msg},
                         {"role": "user", "content": init_user_msg}]
        self.debug_mode = False 

    def get_completion(self, model="gpt-3.5-turbo", temperature=0.8):
        #global total_tokens
        messages = self.messages
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        self.messages.append({"role": "assistant", "content": response.choices[0].message["content"]})
        self.total_tokens = response.usage["total_tokens"]
        #print("Total tokens:", total_tokens)

        if self.debug_mode:
            return response
        else:
            return response.choices[0].message["content"]
    

#****for sphere
  #agentmain=statge1withlumina
agentmain = Agent("agent1_luminastage1", 
                  sphere_systemprompt1+ "please speak short and precise, like natural talking. In 30 words maximum ",
                  "HI! I am Dawnlight Sphere, a creature from other planet", 
                  "", 
                  "30")

  #stage2withlumina
agentmainstage2 = Agent("agent1_luminastage2", 
                  sphere_systemprompt2+ "please speak short and precise, like natural talking. You are very straightforward because of your personality.",
                  "Thanks for trusting me, Lumina, we can know more about each other, I would like to listen to your story and tell you mine", 
                  "", 
                  "40")


  #stage1withglowy
agentmain_glowystage1 = Agent("agent1_glowystage1", 
                  sphere_systemprompt3+ "please speak short and precise, like natural talking. You are very straightforward because of your personality. In 30 words maximum",
                  "HI! I am Dawnlight Sphere, a creature from other planet. I have learned about this island a bit", 
                  "", 
                  "30")

agentmain_glowystage2 = Agent("agent1_glowystage2", 
                  sphere_systemprompt4+ "please speak short and precise, like natural talking. You are very straightforward because of your personality.",
                  "HI! Glowy, let's continue our talk", 
                  "", 
                  "30")


#****for lumina
  #agentlala=luminastage1
agentlala = Agent("lumina", 
                  lumina_systemprompt1+ "you should reply in 40 words maximum", 
                  "Hi, I am lumina, a young light flower who cannot bloom due to lack of light energy.", 
                  "", 
                  "40")

  #agentlala2=luminastage2
agentlala2 = Agent("lumina_stage2", 
                  lumina_systemprompt2+ "you should reply in 40 words maximum", 
                  "OK Dawnlight shpere, let's talk more.", 
                  "", 
                  "50")



Lumina_rating1 = Agent("lumina_detector", 
                  Lumina_rating_prompt1, 
                  "I am a detector, I must strictly follow the instruction to give rating on Lumina's impression, self-esteem, compassion, sentimental, in the format of array.", 
                  "", 
                  "50")

#****for glowy
agentlili = Agent("glowy", 
                  glowy_systemprompt1+ "you should reply in 30 words maximum",
                  "Hi, I am such a pride adult flower, I am very arrogant and I don't like to talk to other creatures",
                  "", 
                  "30")

agentlili2 = Agent("glowy_stage2", 
                  glowy_systemprompt2+ "you should reply in 40 words maximum",
                  "Hi, I am such a pride adult flower, I am very arrogant but I now trust the dawnlight sphere in fromt of me",
                  "", 
                  "30")

Glowy_rating1 = Agent("detector2", 
                  Glowy_rating_prompt1, 
                  "I am a detector, I must strictly follow the instruction to give rating on Glowy's impression, self-esteem, compassion, sentimental, in the format of array.", 
                  "", 
                  "50")


#****for narrator

narrator_exploration=Agent("exploration narrator", 
                  narrator_worldexplorationprompt, 
                  "Here is the narrative for this season, and a short piece of the context of the island. Now you can generate a poetic narrative based on the season you receive. Can be in the style of Haiku.", 
                  "", 
                  "")

narrator_ending=Agent("ending narrator", 
                  narrator_endingprompt, 
                  "Now the story approaching to the end...", 
                  "", 
                  "60")

narrator_ending2=Agent("ending narrator2", 
                  narrator_endingprompt2, 
                  "Now the story approaching to the end...", 
                  "", 
                  "100")

narrator_ending3=Agent("ending narrator3", 
                  narrator_endingprompt3, 
                  "Now the story approaching to the end...", 
                  "", 
                  "100")



def process_serial_data():
    global sensorprompt
    global samplewordword
    global samplesentencesentence
    global lightvalue
    global season
    global narratorword 

    sensor_dict = {
        sensorrange[0]: (sensorpromptlist[0], sampleword[0], samplesentence[0], 1, "summer", narratorpromptlist[0]),
        sensorrange[1]: (sensorpromptlist[1], sampleword[1], samplesentence[1], 2, "summer", narratorpromptlist[1]),
        sensorrange[2]: (sensorpromptlist[2], sampleword[2], samplesentence[2], 3, "summer", narratorpromptlist[2]),
        sensorrange[3]: (sensorpromptlist[3], sampleword[3], samplesentence[3], 4, "summer", narratorpromptlist[3]),
        sensorrange[4]: (sensorpromptlist[4], sampleword[4], samplesentence[4], 5, "spring", narratorpromptlist[4]),
        sensorrange[5]: (sensorpromptlist[5], sampleword[5], samplesentence[5], 6, "spring", narratorpromptlist[5]),
        sensorrange[6]: (sensorpromptlist[6], sampleword[6], samplesentence[6], 7, "spring", narratorpromptlist[6]),
        sensorrange[7]: (sensorpromptlist[7], sampleword[7], samplesentence[7], 8, "spring", narratorpromptlist[7]),
        sensorrange[8]: (sensorpromptlist[8], sampleword[8], samplesentence[8], 9, "autumn", narratorpromptlist[8]),
        sensorrange[9]: (sensorpromptlist[9], sampleword[9], samplesentence[9], 10, "autumn", narratorpromptlist[9]),
        sensorrange[10]: (sensorpromptlist[10], sampleword[10], samplesentence[10], 11, "autumn", narratorpromptlist[10]),
        sensorrange[11]: (sensorpromptlist[11], sampleword[11], samplesentence[11], 12, "autumn", narratorpromptlist[11]),
        sensorrange[12]: (sensorpromptlist[12], sampleword[12], samplesentence[12], 13, "winter", narratorpromptlist[12]),
        sensorrange[13]: (sensorpromptlist[13], sampleword[13], samplesentence[13], 14, "winter", narratorpromptlist[13]),
        sensorrange[14]: (sensorpromptlist[14], sampleword[14], samplesentence[14], 15, "winter", narratorpromptlist[14]),
        sensorrange[15]: (sensorpromptlist[15], sampleword[15], samplesentence[15], 16, "winter", narratorpromptlist[15]),
    }

    while True:
        data_packet = arduinoData.readline()
        data_packet = str(data_packet, 'utf-8')
        data_packet = data_packet.strip('\r\n')

        if data_packet in sensor_dict:
            sensorprompt = sensor_dict[data_packet][0]
            samplewordword = sensor_dict[data_packet][1]
            samplesentencesentence = sensor_dict[data_packet][2]
            lightvalue = sensor_dict[data_packet][3]
            season = sensor_dict[data_packet][4]
            narratorword = sensor_dict[data_packet][5]
        else:
            sensorprompt = "none"
            lightvalue = 0
        #print(samplesentencesentence, lightvalue)



#updating the light value of the sphere           
def send_light_value(client_socket):
    while True:
        lightvalue_message = {"role": "light", "content": lightvalue}
        lightvalue_message_json = json.dumps(lightvalue_message)
        client_socket.sendall(lightvalue_message_json.encode("utf-8"))
        time.sleep(0.2)  # SET SENDING TIME INTERVAL

            


def process_unity_data(client_socket):
    print("process_unity_data function called")  # Debug information
    try:        
        while True:

            unity_data = client_socket.recv(4096).decode('utf-8')
            if not unity_data:
                break#
            print("Received data from Unity:", unity_data)  # Debug information

#Lumina conversation stage1           
            if unity_data == "A":
                agentmain.debug_mode = False
                agentlala.debug_mode = False
                print("emotion now:", sensorprompt)  # Debug print
                #print("emotion now:", process_serial_data())  # Debug print
                agentmain.messages.append({"role": "user", "content":  "your current emotion and behavior is:"+ sensorprompt+ "talking to the flower in front of you under this emotion. You speak short and precise, avoid summarizing the her response but reply to her questions"})
                agentmain_response = agentmain.get_completion()
                agentlala.messages.append({"role": "user", "content": "This is response from Dawnlight sphere:" + agentmain_response+ ", now you can continue the topic or switch to other topics. Rember your personality, you are sentimental and shy so your words should be poetic and short. "})
                print("dawnlightsphere:", agentmain_response, "\n")
                    
                mainagentmessage = {"role": "agentmain", "content": agentmain_response}
                main_agent_message_json = json.dumps(mainagentmessage)
                client_socket.sendall(main_agent_message_json.encode("utf-8"))
                print("Sent data to the main agent client", "\n")
                print("shperetoken:", agentmain.total_tokens)


                lala_response = agentlala.get_completion()
                # agentmain.messages.append({"role": "user", "content": "This is response from Lumina, the flower in front of you: " + lala_response + "."})
                agentmain.messages.append({"role": "user", "content": lala_response})
                print("lumina：", lala_response)
                secondagentmessage = {"role": "agentlala", "content": lala_response}
                lala_agent_message_json = json.dumps(secondagentmessage)
                client_socket.sendall(lala_agent_message_json.encode("utf-8"))
                print("Sent data to the second agent client","\n")
                print("luminatoken:", agentlala.total_tokens)


                Lumina_rating1.messages.append({"role": "user", "content": "This is what dawnlight shpere says: <" + agentmain_response + "> and this is what Lumina says: <" + lala_response + ">"})
                Lumina_rating1_response = Lumina_rating1.get_completion()
                luminaarray = eval(Lumina_rating1_response)
                print("rating", luminaarray)


                LuminaR1message = {"role": "LuminaR1", "content": Lumina_rating1_response}
                LuminaR1message_json = json.dumps(LuminaR1message)
                client_socket.sendall(LuminaR1message_json.encode("utf-8"))
                print("Sent data to the LuminaR1 client", "\n")


                                
               #exceeding the token limit and remind the player for a new start
                if agentmain.total_tokens > 3800:
                    agentlala.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lala_response = agentlala.get_completion()
                    print("lumina:", lala_response)
                    secondagentmessage = {"role": "agentlala", "content": lala_response}
                    lala_agent_message_json = json.dumps(secondagentmessage)
                    client_socket.sendall(lala_agent_message_json.encode("utf-8"))
                    print("Sent data to the second agent client","\n")
                    print("luminatoken:", agentlala.total_tokens)

                    agentlala.messages.clear()
                    agentmain.messages.clear()

                    restartmessage = {"role": "luminarestart", "content": "Lumina loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmain.messages = [{"role": "system", "content": sphere_systemprompt1},
                         {"role": "assistant", "content": "HI! I am Dawnlight Sphere, a creature from other planet"},
                         {"role": "user", "content": ""}]
                    
                    agentlala.messages = [{"role": "system", "content": lumina_systemprompt1},
                            {"role": "assistant", "content": "Hi, I am lumina, a young light flower who cannot bloom due to lack of light energy."},
                            {"role": "user", "content": ""}]
                    
                if agentlala.total_tokens > 3800:
                    agentlala.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lala_response = agentlala.get_completion()
                    print("lumina:", lala_response)
                    secondagentmessage = {"role": "agentlala", "content": lala_response}
                    lala_agent_message_json = json.dumps(secondagentmessage)
                    client_socket.sendall(lala_agent_message_json.encode("utf-8"))
                    print("Sent data to the second agent client","\n")
                    print("luminatoken:", agentlala.total_tokens)
                    agentlala.messages.clear()
                    agentmain.messages.clear()

                    restartmessage = {"role": "luminarestart", "content": "Lumina loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmain.messages = [{"role": "system", "content": sphere_systemprompt1},
                         {"role": "assistant", "content": "HI! I am Dawnlight Sphere, a creature from other planet"},
                         {"role": "user", "content": ""}]
                    
                    agentlala.messages = [{"role": "system", "content": lumina_systemprompt1},
                            {"role": "assistant", "content": "Hi, I am lumina, a young light flower who cannot bloom due to lack of light energy."},
                            {"role": "user", "content": ""}]
                    
        # rating mechanism whether conversation stage 2 starts
                if luminaarray[0] > 0:
                  print("conversation stage2")
                  TPmanager_message = {"role": "TPmanager", "content": "TP1"}
                  TPmanager_message_json = json.dumps( TPmanager_message)
                  client_socket.sendall(TPmanager_message_json.encode("utf-8"))
                  print("Sent data to the TPmanager client", "\n")
                  luminaarray = [0,0,0,2]
                  

                if luminaarray[3] > 5:
                  print("storyending1")
                  TPmanager_message = {"role": "TPmanager", "content": "TP2"}
                  TPmanager_message_json = json.dumps( TPmanager_message)
                  client_socket.sendall(TPmanager_message_json.encode("utf-8"))
                  print("Sent data to the TPmanager client", "\n")


                  print("this is the final ending of the story")
                  narrator_ending2.messages.append({"role": "user", "content": "Lumina, the young flower is extremely sad, compose a story about this flower and how the protagonist, dawnlight shpere leaves the island"})
                  narrator_ending2_response = narrator_ending2.get_completion()
                  print("narrator:", narrator_ending2_response)

                  narrator_message = {"role": "narrator", "content": narrator_ending2_response}
                  narrator_message_json = json.dumps(narrator_message)
                  client_socket.sendall(narrator_message_json.encode("utf-8"))
                  print("Sent data to the narrator client", "\n")
               
#Lumina conversation stage2         
            elif unity_data == "A1":
                agentmainstage2.debug_mode = False
                agentlala2.debug_mode = False
                print("emotion now:", sensorprompt)  # Debug print
                agentmainstage2.messages.append({"role": "user", "content": "your current emotion and behavior is: <" + sensorprompt + ">, talking to lumina under this emotion. You speak short and precise, avoid summarizing the her response but reply to her questions"})
                agentmainstage2_response = agentmainstage2.get_completion()
                agentlala2.messages.append({"role": "user", "content": "This is response from Dawnlight sphere: <" + agentmainstage2_response+ ">, you reply sentimentally, and poetic. Remember you can share your story, tell him about the ways to help him, or mention the adult flower."})
                print("dawnlightsphere_stage2:", agentmainstage2_response, "\n")
                print("shperetoken:", agentmainstage2.total_tokens)      
                mainagentmessage = {"role": "agentmain", "content": agentmainstage2_response}
                main_agent_message_json = json.dumps(mainagentmessage)
                client_socket.sendall(main_agent_message_json.encode("utf-8"))
                print("Sent data to the main agent client", "\n")


                lala2_response = agentlala2.get_completion()
                agentmainstage2.messages.append({"role": "user", "content": "This is response from Lumina, the flower in front of you: <" + lala2_response + ">"})
                print("lumina_stage2:", lala2_response)
                print("shperetoken:", agentlala2.total_tokens)    
                secondagentmessage = {"role": "agentlala", "content": lala2_response}
                lala_agent_message_json = json.dumps(secondagentmessage)
                client_socket.sendall(lala_agent_message_json.encode("utf-8"))
                print("Sent data to the second agent client","\n")

                if agentmainstage2.total_tokens > 3800:
                    agentlala2.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere, tell him you don' want to tell story anymore"})
                    lala2_response = agentlala2.get_completion()
                    print("lumina_stage2:", lala2_response)
                    secondagentmessage = {"role": "agentlala", "content": lala2_response}
                    lala_agent_message_json = json.dumps(secondagentmessage)
                    client_socket.sendall(lala_agent_message_json.encode("utf-8"))
                    print("Sent data to the second agent client","\n")
                    print("luminatoken:", agentlala2.total_tokens)
                    agentlala2.messages.clear()
                    agentmainstage2.messages.clear()

                    restartmessage = {"role": "luminarestart", "content": "Lumina loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmainstage2.messages = [{"role": "system", "content": sphere_systemprompt2},
                         {"role": "assistant", "content": "Thanks for trusting me, Lumina, we can know more about each other, I would like to listen to your story and tell you mine."},
                         {"role": "user", "content": ""}]
                    
                    agentlala2.messages = [{"role": "system", "content": lumina_systemprompt2},
                            {"role": "assistant", "content": "OK Dawnlight shpere, let's talk more, about my past and your past"},
                            {"role": "user", "content": ""}]
                    
                if agentlala2.total_tokens > 3800:
                    agentlala2.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lala2_response = agentlala2.get_completion()
                    print("lumina:", lala2_response)
                    secondagentmessage = {"role": "agentlala", "content": lala2_response}
                    lala_agent_message_json = json.dumps(secondagentmessage)
                    client_socket.sendall(lala_agent_message_json.encode("utf-8"))
                    print("Sent data to the second agent client","\n")
                    print("luminatoken:", agentlala2.total_tokens)
                    agentlala2.messages.clear()
                    agentmainstage2.messages.clear()

                    restartmessage = {"role": "luminarestart", "content": "Lumina loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmainstage2.messages = [{"role": "system", "content": sphere_systemprompt2},
                         {"role": "assistant", "content": "Thanks for trusting me, Lumina, we can know more about each other, I would like to listen to your story and tell you mine."},
                         {"role": "user", "content": ""}]
                    
                    agentlala2.messages = [{"role": "system", "content": lumina_systemprompt2},
                            {"role": "assistant", "content": "OK Dawnlight shpere, let's talk more, about my past and your past"},
                            {"role": "user", "content": ""}]
                    


                if unlockglowystring in lala2_response:
                    print("glowy is unlocked")
                    TPmanager_message = {"role": "TPmanager", "content": "unlockglowy"}
                    TPmanager_message_json = json.dumps( TPmanager_message)
                    client_socket.sendall(TPmanager_message_json.encode("utf-8"))
                    print("Sent data to the TPmanager client", "\n")

                


            elif unity_data == "B":

                agentmain_glowystage1.debug_mode = False
                agentlili.debug_mode = False
                print("emotion now:", sensorprompt)  # Debug print
                agentmain_glowystage1.messages.append({"role": "user", "content":  "your current emotion and behavior is:"+ sensorprompt+ "talking to the flower in front of you under this emotion. You speak short and precise, avoid summarizing the her response but reply to her questions"})
                agentmain_glowystage1_response = agentmain_glowystage1.get_completion()
                agentlili.messages.append({"role": "user", "content": "This is response from Dawnlight sphere:" + agentmain_glowystage1_response+ ", now you can continue the topic or switch to other topics. Rember your personality."})
                print("dawnlightsphere_to_glowy:", agentmain_glowystage1_response, "\n")
                    
                mainagentmessage = {"role": "agentmain", "content": agentmain_glowystage1_response}
                main_agent_message_json = json.dumps(mainagentmessage)
                client_socket.sendall(main_agent_message_json.encode("utf-8"))
                print("Sent data to the main agent client", "\n")
                print("shperetoken:", agentmain_glowystage1.total_tokens)


                lili_response = agentlili.get_completion()
                agentmain_glowystage1.messages.append({"role": "user", "content": "This is response from the flower in front of you: " + lili_response + "."})
                print("Glowy:", lili_response)
                thirdagentmessage = {"role": "agentlili", "content": lili_response}
                lili_agent_message_json = json.dumps(thirdagentmessage)
                client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                print("Sent data to the third agent client","\n")
                print("glowytoken:", agentlili.total_tokens)


                Glowy_rating1.messages.append({"role": "user", "content": "Remember your reply should be in form of array like[0,0,0,0]. This is what dawnlight shpere says: <" + agentmain_glowystage1_response + "> and this is what Glowy says: <" + lili_response + ">"})
                Glowy_rating1_response = Glowy_rating1.get_completion()
                print(Glowy_rating1_response)
                glowyarray = eval(Glowy_rating1_response)
                print("rating", glowyarray)
                #print(Glowy_rating1_response) # Debug information


                GlowyR1message = {"role": "GlowyR1", "content": Glowy_rating1_response}
                GlowyR1message_json = json.dumps(GlowyR1message)
                client_socket.sendall(GlowyR1message_json.encode("utf-8"))
                print("Sent data to the GlowyR1 client", "\n")


                                
               #exceeding the token limit and remind the player for a new start
                if agentmain_glowystage1.total_tokens > 3800:
                    agentlili.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lili_response = agentlili.get_completion()
                    print("glowy:", lili_response)
                    thirdagentmessage = {"role": "agentlili", "content": lili_response}
                    lili_agent_message_json = json.dumps(thirdagentmessage)
                    client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                    print("Sent data to the third agent client","\n")
                    print("glowytoken:", agentlili.total_tokens)

                    agentlili.messages.clear()
                    agentmain_glowystage1.messages.clear()

                    restartmessage = {"role": "glowyrestart", "content": "Glowy loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmain_glowystage1.messages = [{"role": "system", "content": sphere_systemprompt3},
                         {"role": "assistant", "content": "HI! I am Dawnlight Sphere, a creature from other planet"},
                         {"role": "user", "content": ""}]
                    
                    agentlili.messages = [{"role": "system", "content": glowy_systemprompt1},
                            {"role": "assistant", "content": "Hi, I am such a pride adult flower, I am very arrogant and I don't like to talk to other creatures"},
                            {"role": "user", "content": ""}]
                    
                if agentlili.total_tokens > 3800:
                    agentlili.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lili_response = agentlili.get_completion()
                    print("Glowy:", lili_response)
                    thirdagentmessage = {"role": "agentlili", "content": lili_response}
                    lili_agent_message_json = json.dumps(thirdagentmessage)
                    client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                    print("Sent data to the third agent client","\n")
                    print("glowytoken:", agentlili.total_tokens)
                    agentlili.messages.clear()
                    agentmain_glowystage1.messages.clear()

                    restartmessage = {"role": "glowyrestart", "content": "Glowy loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmain_glowystage1.messages = [{"role": "system", "content": sphere_systemprompt3},
                         {"role": "assistant", "content": "HI! I am Dawnlight Sphere, a creature from other planet"},
                         {"role": "user", "content": ""}]
                    
                    agentlili.messages = [{"role": "system", "content": glowy_systemprompt1},
                            {"role": "assistant", "content": "Hi, I am such a pride adult flower, I am very arrogant and I don't like to talk to other creatures"},
                            {"role": "user", "content": ""}]
                    
                if glowyarray[0] > 0:
                  print("glowy conversation stage2")
                  TPmanager2_message = {"role": "TPmanager2", "content": "TP3"}
                  TPmanager2_message_json = json.dumps( TPmanager2_message)
                  client_socket.sendall(TPmanager2_message_json.encode("utf-8"))
                  print("Sent data to the TPmanager2 client", "\n")
                  glowyarray = [0,0,0,0]
                  

                if glowyarray[3] > 5:
                  print("storyending2")
                  TPmanager2_message = {"role": "TPmanager2", "content": "TP4"}
                  TPmanager2_message_json = json.dumps( TPmanager2_message)
                  client_socket.sendall(TPmanager2_message_json.encode("utf-8"))
                  print("Sent data to the TPmanager2 client", "\n")


                  print("this is the final ending of the story")
                  narrator_ending3.messages.append({"role": "user", "content": "Glowy, the adult flower is extremely sad, compose a story about this flower and how the protagonist, dawnlight shpere leaves the island"})
                  narrator_ending3_response = narrator_ending3.get_completion()
                  print("narrator:", narrator_ending3_response)

                  narrator_message = {"role": "narrator", "content": narrator_ending3_response}
                  narrator_message_json = json.dumps(narrator_message)
                  client_socket.sendall(narrator_message_json.encode("utf-8"))
                  print("Sent data to the narrator client", "\n")

            elif unity_data == "B1":

                agentmain_glowystage2.debug_mode = False
                agentlili2.debug_mode = False
                print("emotion now:", sensorprompt)  # Debug print
                agentmain_glowystage2.messages.append({"role": "user", "content":  "your current emotion and behavior is:"+ sensorprompt+ "talking to the flower in front of you under this emotion. You speak short and precise, avoid summarizing the her response but reply to her questions"})
                agentmain_glowystage2_response = agentmain_glowystage2.get_completion()
                agentlili2.messages.append({"role": "user", "content": "This is response from Dawnlight sphere:" + agentmain_glowystage2_response+ ", now you can continue the topic or switch to other topics. Rember your personality."})
                print("dawnlightsphere_to_glowy_stage2:", agentmain_glowystage2_response, "\n")
                    
                mainagentmessage = {"role": "agentmain", "content": agentmain_glowystage2_response}
                main_agent_message_json = json.dumps(mainagentmessage)
                client_socket.sendall(main_agent_message_json.encode("utf-8"))
                print("Sent data to the main agent client", "\n")
                print("shperetoken:", agentmain_glowystage2.total_tokens)


                lili2_response = agentlili2.get_completion()
                agentmain_glowystage2.messages.append({"role": "user", "content": "This is response from the flower in front of you: " + lili2_response + "."})
                print("Glowy_stage2:", lili2_response)
                thirdagentmessage = {"role": "agentlili", "content": lili2_response}
                lili_agent_message_json = json.dumps(thirdagentmessage)
                client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                print("Sent data to the third agent client","\n")
                print("glowytoken:", agentlili2.total_tokens)

                                
               #exceeding the token limit and remind the player for a new start
                if agentmain_glowystage2.total_tokens > 3800:
                    agentlili2.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lili2_response = agentlili2.get_completion()
                    print("glowy:", lili2_response)
                    thirdagentmessage = {"role": "agentlili", "content": lili2_response}
                    lili_agent_message_json = json.dumps(thirdagentmessage)
                    client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                    print("Sent data to the third agent client","\n")
                    print("glowytoken:", agentlili2.total_tokens)

                    agentlili2.messages.clear()
                    agentmain_glowystage2.messages.clear()

                    restartmessage = {"role": "glowyrestart", "content": "Glowy loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmain_glowystage2.messages = [{"role": "system", "content": sphere_systemprompt4},
                         {"role": "assistant", "content": "HI! I am Dawnlight Sphere, a creature from other planet"},
                         {"role": "user", "content": ""}]
                    
                    agentlili2.messages = [{"role": "system", "content": glowy_systemprompt2},
                            {"role": "assistant", "content": "Hi, I am such a pride adult flower, I am very arrogant and I don't like to talk to other creatures"},
                            {"role": "user", "content": ""}]
                    
                if agentlili2.total_tokens > 3800:
                    agentlili2.messages.append({"role": "user", "content": "you should behave now you are losing your patience, and want to say goodbye to the shpere."})
                    lili2_response = agentlili2.get_completion()
                    print("Glowy:", lili2_response)
                    thirdagentmessage = {"role": "agentlili", "content": lili2_response}
                    lili_agent_message_json = json.dumps(thirdagentmessage)
                    client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                    print("Sent data to the third agent client","\n")
                    print("glowytoken:", agentlili2.total_tokens)
                    agentlili2.messages.clear()
                    agentmain_glowystage2.messages.clear()

                    restartmessage = {"role": "glowyrestart", "content": "Glowy loses her patience...You have to start over again the conversation."}
                    restart_agent_message_json = json.dumps(restartmessage)
                    client_socket.sendall(restart_agent_message_json.encode("utf-8"))


                    agentmain_glowystage2.messages = [{"role": "system", "content": sphere_systemprompt4},
                         {"role": "assistant", "content": "HI! I am Dawnlight Sphere, a creature from other planet"},
                         {"role": "user", "content": ""}]
                    
                    agentlili2.messages = [{"role": "system", "content": glowy_systemprompt2},
                            {"role": "assistant", "content": "Hi, I am such a pride adult flower, I am very arrogant and I don't like to talk to other creatures"},
                            {"role": "user", "content": ""}]
                
                if unlockendingstring in lili2_response:
                    print("Ending3, final ending is unlocked")
                    TPmanager_message = {"role": "TPmanager", "content": "unlockfinalending"}
                    TPmanager_message_json = json.dumps( TPmanager_message)
                    client_socket.sendall(TPmanager_message_json.encode("utf-8"))
                    
                    print("this is the final ending of the story")
                    narrator_ending.messages.append({"role": "user", "content": "This is from glowy:" + lili2_response})
                    narrator_ending_response = narrator_ending.get_completion()
                    print("narrator:", narrator_ending_response)

                    narrator_message = {"role": "narrator", "content": narrator_ending_response}
                    narrator_message_json = json.dumps(narrator_message)
                    client_socket.sendall(narrator_message_json.encode("utf-8"))
                    print("Sent data to the narrator client", "\n")


            elif unity_data == "C":
                print("this flower refuse to talk to you")
                thirdagentmessage = {"role": "agentlili", "content": "This flower refuse to talk to you"}
                lili_agent_message_json = json.dumps(thirdagentmessage)
                client_socket.sendall(lili_agent_message_json.encode("utf-8"))
                print("Sent data to the third agent client","\n")

            elif unity_data == "D":
                print("this is the general narrative")
                narrator_exploration.messages.append({"role": "user", "content": season + "This is the context: " + narratorword})
                print(season)
                narrator_exploration_response = narrator_exploration.get_completion()
                print("narrator:", narrator_exploration_response)

                narrator_message = {"role": "narrator", "content": narrator_exploration_response}
                narrator_message_json = json.dumps(narrator_message)
                client_socket.sendall(narrator_message_json.encode("utf-8"))
                print("Sent data to the narrator client", "\n")





    except ConnectionResetError:
        print("Connection with Unity was reset by the host machine.")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close client connection
        client_socket.close()


serial_thread = threading.Thread(target=process_serial_data, daemon=True)
serial_thread.start()

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print("Client connected from", client_address)

    try:
        
        # thread send light value 
        lightvalue_thread = threading.Thread(target=send_light_value, args=(client_socket,))
        lightvalue_thread.daemon = True
        lightvalue_thread.start()

        # Create a thread to handle Unity data
        unity_thread = threading.Thread(target=process_unity_data, args=(client_socket,))
        #unity_thread.daemon = True
        unity_thread.start()


    except Exception as e:
        print("Error:", e)
