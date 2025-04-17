# Document Summarization using LLM

I used the `docsum.py` file to request the **meta-llama/llama-4-scout-17b-16e-instruct** model from **GROQ** to summarize texts or images for me. For now, the program can summarize files including txt files, html files, pdf files, images, and webpages by providing URLs. 

## How to Use the Program
### For HTML files:  
Example command:
```
python3 docsum.py docs/news-mx.html
```
You will get results similar to:  


The US Supreme Court has allowed President Donald Trump to continue using a 1798 war-era law to deport Venezuelan immigrants accused of belonging to a criminal gang. The decision, made by 5 conservative judges versus 4 progressive judges, lifts a temporary suspension on deportations, but requires immigrants to have the opportunity to challenge their deportation before being expelled. The law, known as the Alien Enemy Act, has been questioned for its application in this case, as there is no declared war between the US and Venezuela.


  

### For TXT files:  
Example command:
```
python3 docsum.py docs/constitution-mx.txt
```
You will get results similar to:  
  
La Constitución Mexicana de 1917, modificada hasta 2010, establece las leyes y principios fundamentales de los Estados Unidos Mexicanos, garantizando derechos y libertades individuales, incluyendo los de los pueblos indígenas, y limitando el poder del gobierno. La constitución garantiza el derecho a la educación, salud, vivienda digna, un medio ambiente adecuado y acceso a la cultura, y protege la libertad de trabajo y profesión. También establece principios para el desarrollo nacional, como la rectoría del Estado en la planeación democrática del desarrollo nacional y la protección de la actividad económica de los particulares.

     
### For PDF files:  
  Example command:
  ```
python3 docsum.py docs/research_paper.pdf
  ```
  You will get results similar to:  
A survey of 1,500 students at a large US public university found that the COVID-19 pandemic had significant negative effects on students' experiences and expectations, including delayed graduation, lost jobs or internships, and decreased expected earnings. The pandemic's impact was particularly pronounced for students from disadvantaged backgrounds, including lower-income students, racial minorities, and first-generation students, who experienced larger negative impacts on their academic outcomes. Policymakers may be able to mitigate these effects by addressing the economic and health impacts of the pandemic, which could help prevent the pandemic from exacerbating existing socioeconomic divides in higher education.
    
  
### For Images:  
  Example command (You can directly provide the URL of the image):
```
python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
```
  You will get results similar to:  
  **Summary of the image:**   
  The image depicts a modern building with a glass-enclosed structure, featuring a pool of water in front of it. The scene is set at dusk.

**Key Features:**

* A glass-enclosed structure with a flat roof and a black frame
* A pool of water in front of the structure, reflecting the lights from inside
* A large building to the right with multiple floors and balconies
* A smaller building to the left with a flat roof and several windows
* A dark blue sky with clouds

**Atmosphere:**

* The overall atmosphere suggests a peaceful and serene setting, possibly a hotel or office building
* The use of glass and modern design elements creates a sense of openness and sophistication

**Color Scheme:**

* The dominant colors are shades of blue, orange, yellow, and black, which create a warm and inviting ambiance.

    
### Webpages  
Example command (You can directly provide the URL of the webpage):
```
python3 docsum.py https://elpais.com/us/
```
You will get results similar to:  
**Summary of the webpage:**  
The provided text appears to be a collection of technical code snippets, including JavaScript and CSS styles, used for website development, specifically for El Pais, a Spanish news website. The code sets up configurations, defines functions, and styles various elements for the website, but does not contain any readable content or narrative. However, a news snippet at the end reports on the death of Mario Vargas Llosa, a Peruvian-Spanish writer and Nobel laureate.  

**Summary of the document:**  
There is no text to summarize. The provided text appears to be a collection of code snippets, including JavaScript and CSS, used for a website, likely El Pais, a Spanish news organization, as well as some news summaries. However, if you'd like to provide actual text from an article, I can summarize it for you in 1-3 sentences.  


## Additional Notes: 
The project is produced under the instructions of [CMC-CSCI040](https://github.com/mikeizbicki/cmc-csci040/tree/2025spring/topic_10_Python_LLMs).   
The summarization of images is produced with the instructions from [GroqCould](https://console.groq.com/docs/vision).   
The [LLM Model](https://console.groq.com/playground) is used on the platform of Groq. 

