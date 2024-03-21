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

[TO BE UPDATED]

# Prompt

Although the detailed prompt is listed in the file， here we summarize the prompt we applied~

| 情绪  | VALENCE | 行为                                        | 可以使用的词汇                                | 示例句子                                                                                             |
|-------|---------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------|
| 愤怒  | 1-64    | 1-16 (低)                                    | "我受够了！" "挡在我面前，免得我发火。" "我简直无法相信你会做出这样的事情。" "越过了底线" "我不再克制了。" | "我已经受够了这一切！你的行为完全无法接受，我不能容忍。你已经越过了底线，我不会再容忍下去。准备好了，因为我不再克制自己。" |

