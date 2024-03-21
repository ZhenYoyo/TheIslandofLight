# The Island of Light

# Contents
- [Intro](#Intro)
- [Code](#code)
- [NarrativeScript](#narrativescript)
- [Prompt](#prompt)

# Intro

Hello~ Welcome to the Island of Light. It is an emergent narrative that links the storytelling with the tangible and embodied data captured from the controller. 

The game scene:
Where the protagonist, Dawnlight Sphere meet the young flower，Lumina
  
![game2](https://github.com/ZhenYoyo/TheIslandofLight/assets/138093070/616e0e6c-b85b-4761-bdf9-d986d99172bd)

The real playing scenario:
The player can control the emotional tone of the generated text content, by changing the light received from the tangible controller~

![Picture1](https://github.com/ZhenYoyo/TheIslandofLight/assets/138093070/2e4255b4-e723-400f-8e90-b854b9187d0e)


# Code
This repository has mainly three components for running the demo. 😊

## python code：
[main]12.27.py

The python code is the main part to control the text generation, including the prompt defining, state transition of the narrative.

REMEMBER: 

#replace the api key/base with your own key/base~

#connecting to your device like Arduino Uno/Esp32...., please replace'COM4' with the actual one your are using. you can change the analog read port based on the controller that you are using~


## unity package(file)：

Open UnityPackageSource.txt

You should find the link where you can download the unity source package~ 

## arduino code:

controller.ino

very very simple code for getting data from your sensing device. In the game, I used ambient light sensor~


##
Run the three part simutaneously on your PC~



# NarrativeScript

Here is the demo of the whole narration experienced by different playthrough


## Narrative History Example 1 - Ending 1

Dawnlightsphere: Hey there, flower! Just wanted to let you know that I come from a rich planet 
where I never fail. I'm here to get to know this island better, and I'm confident I'll accomplish that! 
#accomplishment #fulfill my expectations #achievement

Lumina：I hate this behavior of you...GO AWAY PLEASE!

rating [-1, -1, 0, 3]


Dawnlightsphere: Oh my goodness! I never expected such a strong reaction from you. I'm sorry if my 
behavior was not to your liking. I'll respect your wish and leave.


Lumina： Better...I...leave.

rating [-1, -1, 0, 5]

Dawnlightsphere: Wow! I feel like I could fly! My heart is racing with joy. Thank you for allowing me to 
stay. I'm excited to learn more about this island!

Lumina：OK...OK... Let me share with you my view on death. While I may seem indifferent, within me 
lies cherished memories that make me hesitate to give up on life. Death is but a means to prove that 
we have truly lived.

rating [1, 0, 0, 5]

---conversation stage2
this flower refuse to talk to you


Dawnlightsphere_stage2: Lumina, I am a traveler here, and I am stuck on this island, looking for a way 
to leave.

Lumina_stage2: Ah, dear traveler, lost in this island's embrace. I too long for escape from my 
perpetual darkness. Deep within the mud lies a sealed spacecraft ticket, waiting to be freed. If you 
could help me absorb more light energy, we could unlock its power.

Dawnlightsphere_stage2: Lumina, I understand your desire to escape the darkness and find a way out. 
Absorbing more light energy to unlock the spacecraft ticket is a worthy goal. How can I assist you in 
absorbing more light energy?

Lumina_stage2: Dear Dawnlight Sphere, your willingness to help fills my fragile heart with hope. To 
absorb more light energy, I need the assistance of the adult flower. With its power, I can bloom and 
gather enough energy to unlock the sealed ticket. Please, help me, and together, we can find a way 
out of this darkness. 

---glowy is unlocked & dawnlight shpere went to find glowy

Dawnlightsphere_to_glowy: Your emotion is: Elation
"Hello, beautiful flower! I'm Dawnlight Sphere, and I am absolutely thrilled to meet you! My heart is 
racing with excitement, and I feel like I could fly! How can I help you today?"

Glowy: Hmm, well, I suppose it's nice to be appreciated. But really, there's nothing special about me. 
I'm just a flower with one less petal than the others. It's hard to feel elated when you're constantly 
reminded of your flaws. But enough about me, tell me, what brings you to this island?
rating [1, -1, 0, 0]

glowy conversation stage2


Dawnlightsphere_to_glowy_stage2: Glowy, I have come to ask for your help. Lumina, a young flower, 
needs your power to grow. I believe that you possess something that can aid her growth. I am 
confident in your abilities and know that you can fulfill my expectations. Can you please assist Lumina 
in her journey to become stronger?

Glowy_stage2: I am ready to give you the thing you want, here is one of my petals. Use it to help 
Lumina grow and become stronger. But remember, I am doing this because I trust you, not because I 
like you. Don't disappoint me.

Ending3, final ending is unlocked
this is the final ending of the story
Narrator: With Glowy's last words echoing in Dawnlight Sphere's mind, they carefully cradled the 
precious petal in their luminous hands. The petal radiated a soft glow, pulsating with power and 
potential. Dawnlight Sphere felt a surge of determination, knowing that this gift held the key to 
saving Lumina from her despair.
Returning to Lumina's side, Dawnlight Sphere gently placed the petal next to her wilted form. As if 
sensing the presence of the petal, Lumina's petals twitched slightly, a faint glimmer of hope flickering 
in her dimming light. Dawnlight Sphere whispered soothing words, urging Lumina to hold on just a 
little longer. 
With a surge of energy, Lumina absorbed the petal's essence, its light infusing every fiber of her being. 
The once-faded colors of her petals were now vibrant and alive, her stem strengthened, and her 
fragile form radiated with newfound strength. Lumina's spirit soared as she felt her power returning, 
rejuvenating her from within.
As the days passed, Lumina flourished under the guidance of Dawnlight Sphere. Together, they 
explored the island of light, spreading Lumina's radiance to every corner, ilLuminating even the 
darkest recesses. The island, once shrouded in gloom, now glowed with an ethereal brilliance, 
attracting creatures from far and wide who basked in Lumina's light.
Word of Lumina's transformation spread beyond the island, reaching the ears of other flowers and 
creatures who were lost and in need of hope. Inspired by Lumina's resilience, they sought her 
guidance, her light becoming a beacon of courage and solace for those in despair.
Lumina, now an adult flower, realized the power of her light was not just for herself but for all who 
needed it. With Dawnlight Sphere by her side, they embarked on a journey to spread hope and 
healing to all the realms. Together, Lumina and Dawnlight Sphere became symbols of strength and 
resilience, forever changing the lives they touched.
And so, the Island of Light shone brighter than ever before, a testament to the indomitable spirit of 
Lumina and the unwavering faith of Dawnlight Sphere. Their story of redemption and triumph 
became a legend, whispered by flowers and creatures alike, reminding them that even in the darkest 
of times, there is always a glimmer of light, ready to ignite the spark of hope.


## Narrative History Example 2 - Ending2

summer
Narrator: Petals heavy with rain,
Light Flowers sway in the breeze,
Summer's melody.

summer
Narrator: Petals hold rain's weight,
Melodic notes fill the air,
Rain Festival starts.

summer
Narrator: Rainwater jewels gleam,
Petals laden with the sky's tears,
Music of the Rain Festival.
Sent data to the Narrator client

summer
Narrator: Raindrops on petals,
Melodic symphony plays,
Summer's Rain Festival.

autumn
Narrator: Baldies shed their crowns,
Mocked by others, yet they thrive,
Strength in vulnerability.
autumn

Narrator: Rhizomes reach for light,
Mountain ranges unite strong,
Winter's preparation.

autumn
Narrator: Petals drift away,
Baldies face taunts and scorn,
Strength in vulnerability.

summer
Narrator: Petals hold rain's weight,
Melodic notes fill the air,
Summer's Rain Festival.

autumn
Narrator: Baldies lose petals,
Mocked by others, yet they thrive,
Strength in vulnerability.

winter
Narrator: Rhizomes entwined tight,
Seeking to outshine the rest,
Winter's tangled dance.

winter
Narrator: Rhizomes battle on,
Entwined in winter's embrace,
Twisted tales of growth.

dawnlightsphere: What did you do to my light energy? It is not yours to take. Return it to me 
immediately. 


lumina： Better...I...leave.
rating [0, -1, 0, 3]


dawnlightsphere: I am the Dawnlight Sphere, a being of light and grace. I deserve respect and honor. 
Tell me about this island's secrets, and I may grace you with my presence.

lumina： I think I should stop talking...to be honest.
rating [-1, -1, 0, 5]


dawnlightsphere: Your loss. I am a being of light and grace, and you will regret not seeking my 
wisdom. Farewell, insignificant flower.
lumina： Better...I...leave.
rating [0, -2, 0, 8]

storyending1
this is the final ending of the story
Narrator: Once a vibrant and beautiful flower, Lumina had lost all her energy and hope. She no longer 
felt the warmth of the sun or the gentle caress of the wind. The weight of sadness crushed her petals, 
and she could no longer find joy in blooming.
As days passed, Lumina's colors faded, and her once lively spirit wilted. The other flowers watched in 
sorrow as their friend withered away, unable to find a way to bring back her light.
Several months later, Dawnlight Sphere, the protector of the island, sensed the heavy aura that 
lingered over Lumina. With a heavy heart, she made the difficult decision to leave the island, knowing 
that she had done all she could to help Lumina. As she departed, a single tear fell from her eye, 
carrying with it the memory of the flower that had lost her spark. 

# Prompt

+ chat history example

+ full prompt list
[although the detailed prompt is listed in the file， here we summarize the prompt doc we use]

