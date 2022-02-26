 <img src = "https://drive.google.com/uc?export=view&id=1uSO3lyjBBNwF7WbjJNcRnYrchpkJCQGR" width="220" height="45">   

**Authors:** Shashank Ojha, Andreas Joannou, Abdellah Ghassel, Cameron Smith 

Update: Winner of the best wearable gadget in the UofT Makeathon 2022

## Inspiration
  
 <p align="center">  
<img src = "https://drive.google.com/uc?export=view&id=1griTlDOUhpmhqq7CLNtwrQnRGaBXGn72" width="300" height="300">   
 </p>

Clarity is an interactive smart glass that uses a convolutional neural network, to notify the user of the emotions of those in front of them. This wearable gadget has other smart glass abilities such as the weather and time, viewing daily reminders and weekly schedules, to ensure that users get the best well-rounded experience. 


## Problem:
As mental health raises barriers inhibiting people's social skills, innovative technologies must accommodate everyone. Studies have found that individuals with developmental disorders such as Autism and Asperger’s Syndrome have trouble recognizing emotions, thus hindering social experiences. For these reasons, we would like to introduce Clarity. Clarity creates a sleek augmented reality experience that allows the user to detect the emotion of individuals in proximity. In addition, Clarity is integrated with unique and powerful features of smart glasses including weather and viewing daily routines and schedules. With further funding and development, the glasses can incorporate more inclusive features straight from your fingertips and to your eyes. 

<p align="center">  
<img src = "https://drive.google.com/uc?export=view&id=1eVZFYgQIm7vu5UOjp5tvgFOxvf3kv4Oj" width="300" height="300">   
<img src = "https://drive.google.com/uc?export=view&id=1L-5w9jzwKG0dLdwe-OCMUa6S2HnZeaFo" width="300" height="300">
<img src = "https://drive.google.com/uc?export=view&id=1LP7bI9jAupQDQcfbQIszs9igVEFSuqDb" width="300" height="300">
 
 </p>

## Mission Statement:

At Clarity, we are determined to make everyone’s lives easier, specifically to help facilitate social interactions for individuals with developmental disorders. Everyone knows someone impacted by mental health or cognitive disabilities and how meaningful those precious interactions are. Clarity wants to leap forward to make those interactions more memorable, so they can be cherished for a lifetime.


<p align="center">  
<img src = "https://drive.google.com/uc?export=view&id=1qJgJIAwDI0jxhs1Q59WyaGAvFg5fysTt" width="300" height="300"> 
<img src = "https://drive.google.com/uc?export=view&id=1AY5zbgfUB4c_4feWVVrQcuOGtn_yGc99" width="400" height="300"> 
 </p>

We are first-time Makeathon participants who are determined to learn what it takes to make this project come to life and to impact as many lives as possible.  Throughout this Makeathon, we have challenged ourselves to deliver a well-polished product that, with the purpose of doing social good. We are second-year students from Queen's University who are very passionate about designing innovative solutions to better the lives of everyone. We share a mindset to give any task our all and obtain the best results. We have a diverse skillset and throughout the hackathon, we utilized everyone's strengths to work efficiently. This has been a great learning experience for our first makeathon, and even though we have some respective experiences, this was a new journey that proved to be intellectually stimulating for all of us.

## About: 

### Market Scope: 
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=10LWCDhgfDPp1scpVI1GSAGIWrjprQtOY" width="400" height="400"> 
  </p>
Although the main purpose of this device is to help individuals with mental disorders, the applications of Clarity are limitless. Other integral market audiences to our device include:


  •	Educational Institutions can use Clarity to help train children to learn about emotions and feelings at a young age. Through exposure to such a powerful technology, students can be taught fundamental skills such as sharing, and truly caring by putting themselves in someone else's shoes, or lenses in this case.

  •	The interview process for social workers can benefit from our device to create a dynamic and thorough experience to determine the ideal person for a task. It can also be used by social workers and emotional intelligence researchers to have better studies and results. 
  
  •	With further development, this device can be used as a quick tool for psychiatrists to analyze and understand their patients at a deeper level. By assessing individuals in need of help at a faster level, more lives can be saved and improved.  
  
### Whats In It For You:
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1XbrcnIEc3eAYDmkopmwGbSew11GQv91v" width="500" height="400"> 
  </p>
 
The first stakeholder to benefit from Clarity is our users. This product provides accessibility right to the eye for almost 75 million users (number of individuals in the world with developmental disorders).  The emotion detection system is accessible at a user's disposal and makes it easy to recognize anyone's emotions. Whether one watching a Netflix show or having a live casual conversation, Clarity has got you covered. 

Next, Qualcomm could have a significant partnership in the forthcoming of Clarity, as they would be an excellent distributor and partner. With professional machining and Qualcomm's Snapdragon processor, the model is guaranteed to have high performance in a small package. 

Due to the various applications mentioned of this product, this product has exponential growth potential in the educational, research, and counselling industry, thus being able to offer significant potential in profit/possibilities for investors and researchers. 

# Technological Specifications

## Hardware:
At first, the body of the device was a simple prism with an angled triangle to reflect the light at 90° from the user. The initial intention was to glue the glass reflector to the outer edge of the triangle to complete the 180° reflection. This plan was then scrapped in favour of a more robust mounting system, including a frontal clip for the reflector and a modular cage for the LCD screen. After feeling confident in the primary design, a CAD prototype was printed via a 3D printer. During the construction of the initial prototype, a number of challenges surfaced including dealing with printer errors, component measurement, and manufacturing mistakes. One problem with the prototype was the lack of adhesion to the printing bed. This resulted in raised corners which negatively affected component cooperation. This issue was overcome by introducing a ring of material around the main body. Component measurements and manufacturing mistakes further led to improper fitting between pieces. This was ultimately solved by simplifying the initial design, which had fewer points of failure. The evolution of the CAD files can be seen below.
 
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1vDT1gGyfM7FgioSRr71yBSysGntOfiFC" width="400" height="400"> 
  </p>
  
The material chosen for the prototypes was PLA plastic for its strength to weight ratio and its low price. This material is very lightweight and strong, allowing for a more comfortable experience for the user. Furthermore, inexpensive plastic allows for inexpensive manufacturing.

Clarity runs on a Raspberry Pi Model 4b. The RPi communicates with the OLED screen using the I2C protocol. It additionally powers and communicates with the camera module and outputs a signal to a button to control the glasses. The RPi handles all the image processing, to prepare the image for emotion recognition and create images to be output to the OLED screen.


### Optics:

Clarity uses two reflections to project the image from the screen to the eye of the wearer. The process can be seen in the figure below.  First, the light from the LCD screen bounces off the mirror which has a normal line oriented at 45° relative to the viewer. Due to the law of reflection, which states that the angle of incidence is equal to the angle of reflection relative to the normal line, the light rays first make a 90° turn. This results in a horizontal flip in the projected image. Then, similarly, this ray is reflected another 90° against a transparent piece of polycarbonate plexiglass with an anti-reflective coating. This flips the image horizontally once again, resulting in a correctly oriented image. The total length that the light waves must travel should be equivalent to the straight-line distance required for an image to be discernible. This minimum distance is roughly 25 cm for the average person. This led to shifting the screen back within the shell to create a clearer image in the final product.

<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1dOHIXN2L045LHh7rCoD0iTrW_IVKf7dz" width="200" height="200"> 
  </p>
  

## Software: 
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1DzqhM4p5y729deKQQkTw5isccUeZRCP8" width="600" height="400"> 
  </p>
  
The emotion detection capabilities of Clarity smart glasses are powered by Google Cloud Vision API. The glasses capture a photo of the people in front of the user, runs the photo through the Cloud Vision model using an API key, and outputs a discrete probability distribution of the emotions. This probability distribution is analyzed by Clarity’s code to determine the emotion of the people in the image. The output of the model is sent to the user through the OLED screen using the Pillow library.

The additional features of the smart glasses include displaying the current time, weather, and the user’s daily schedule. These features are implemented using various Python libraries and a text file-based storage system. Clarity allows all the features of the smart glasses to be run concurrently through the implementation of asynchronous programming. Using the asyncio library, the user can iterate through the various functionalities seamlessly.

The glasses are interfaced through a button and the use of Siri. Using an iPhone, Siri can remotely power on the glasses and start the software. From there, users can switch between the various features of Clarity by pressing the button on the side of the glasses.

The software is implemented using a multi-file program that calls functions based on the current state of the glasses, acting as a finite state machine. The program looks for the rising edge of a button impulse to receive inputs from the user, resulting in a change of state and calling the respective function.

## Next Steps: 
The next steps include integrating a processor/computer inside the glasses, rather than using raspberry pi. This would allow for the device to take the next step from a prototype stage to a mock mode. The model would also need to have Bluetooth and Wi-Fi integrated, so that the glasses are modular and easily customizable. We may also use magnifying lenses to make the images on the display bigger, with the potential of creating a more dynamic UI.

## Timelines:
As we believe that our device can make a drastic impact in people’s lives, the following diagram is used to show how we will pursue Clarity after this Makathon:

<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1m85rTMVAqIIK5VRbjqESn1Df-H0Pilx8" width="500" height="700"> 
</p>

## References: 

•	https://cloud.google.com/vision

•	Python Libraries 
### Hardware: 
All CADs were fully created from scratch. However, inspiration was taken from conventional DIY smartglasses out there.

### Software: 

### Research:
•	https://www.vectorstock.com/royalty-free-vector/smart-glasses-vector-3794640

•	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2781897/

•	https://www.google.com/search?q=how+many+people+have+autism&rlz=1C1CHZN_enCA993CA993&oq=how+many+people+have+autism+&aqs=chrome..69i57j0i512l2j0i390l5.8901j0j9&sourceid=chrome&ie=UTF-8

•	(http://labman.phys.utk.edu/phys222core/modules/m8/human_eye.html)

•	https://mammothmemory.net/physics/mirrors/flat-mirrors/normal-line-and-two-flat-mirrors-at-right-angles.html
