
سلام 
هدف از انجام این تسک، توسعه یک اپلیکیشن بازشناسی گفتار برای زبان فارسی می‌باشد.
برای این کار از مدل های موجود در kaldi و از پارپوب توسعه ی vosk استفاده شد.
اکد مربوط به این تسک به چهار قسمت تقسیم شده : 
<br>1-recording audio <br>
در این بخش ضبط صدا ما با استفاده از یک کد html یک لاین برای ضبط صدا ایجاد کرده و آنرا اجرا میکنیم و کاربر با فشار دادن دکمه به رایند ضبط خاتمه میدهد. سپس با پردازش بر روی صوت ضبط شده آن را به فرمت wav در آورده و نرمال سازی را نیز انجام میدهیم. به این ترتیب توانستیم درمحیط کولب به میکروفون وصل شده و صدای خود را به فرمت دلخواه ضبط کنیم.
<br>2-Vosk models<br>
در این بخش خود از دو زیربخش تشکیل شده در زیربخش اول (downloading models from vosk) مدل های pre-train شده‌ی زبان فارسی در در سایت Vosk قرار دارد، دانلود شده و در پوشه ی دلخواه ذخیره میشود. در زیربخش یعدی به توسعه model پرداختیم و سه مدل مختلف وسک را اجرا کردیم و recognizer مربوط به هر کدام را ایجاد کردیم. 
<br>3-test<br>
در قسمت تست ما یک فایل صوتی ریکورد کردیم و نتایج مربوط به هر مدل را بررسی کردیم
<br>4-resualt<br>
در پایان با استفاده از نتایج به دست آمده، Word Error Rate را محاسبه کردیم. نتیجه هر سه مدل با هم برابر بود زیرا خروجی مدل ها یکی بود. 


<br><br><br>Hello
<br>This task aims to develop a speech recognition application for the Persian language.
<br>The models available in Kaldi and Vosk framework were used for this work.
<br>The code related to this task is divided into four parts:
<br>1-recording audio
 <br>This is the recording section, I use an HTML code to create a line for voice recording and run it, and the user ends the recording process by pressing the button. Then, by processing the recorded sound, I convert it into a suitable format and perform normalization. In this way, I was able to connect to the microphone and record my voice in the desired format
<br>2-Vosk models
<br>This section consists of two sub-sections; in the first sub-section (downloading models from Vosk), pre-trained Persian language models are located on the Vosk website, downloaded, and saved in the desired folder. In the other sub-section, I developed the model, implemented three different Vosk pre-trained models, and created a recognizer for each.
<br>3-test
<br>In the test section, we recorded an audio file and checked the results for each model
<br>4-results
<br>In the end, using the obtained results, I calculated the Word Error Rate. The results for all three models were equal because the output of the models was the same.
