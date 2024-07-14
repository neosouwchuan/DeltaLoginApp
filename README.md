# DeltaLoginApp
My attempt at solving a problem of signing into OCS Service Term digitally.
For those that are not from Singapore, all Singaporean males are drafted for up to 2 years after reaching 16(or later if they defer due to studies). During conscription, some are sent to OCS for training, and OCS is made up of 3 terms which service terms is about 3 months. During my 3 months in Delta Wing, I contributed what I could to my Wing by trying to introduce digital signing in because signing in by hand took a lot of time. 
The requirements are as follows:
Anonymity(Under PDPA laws I am not allowed to store anything such as NRIC (Unique Identifier)/ Fingerprint/ Face Image and other related Biometric data).
No permanent pictures allowed to be stored on device.
Faster than physically signing in.
Cadet signing in must be within the wingline(IE not just at the gate of the camp).
No method to fake signing in time.

Given this requirements there were 2 possible methods:
An app that would check the geolocation if it is within a certain radius of wingline, and if so would send a post request to a server to say a specific person signed in. Pros is that it is very convenient for cadets. However it is also unecessarily exposed to the internet and easy to spoof with more technologically savvy cadets.

Based of the cons of this, scanning a QR code seems to be the next logical choice, my system would involve a QR code app generator and a QR code scanner on the airgapped laptop. Importantly most scanners are coded as a keyboard that inputs a string of text after scanning a valid code. This is essential so I dont trigger any security alarms. The content of the QR code will be a string which contains the 4d of the person, the datetime of the qr code generation, and a bit of basic encryption. The security systems I have in place are quite basic but make it difficult to surpass, not that in OCS anybody has time to crack systems for a little benefit. The 4D, which is the unique identifier of the person, is firstly slightly altered based on first sign in date, so its impossible for another person to reinstall the app and input another person's 4d to fake a sign in, additionally the qr code also contains the time create for the qr code so the scanner knows whether the qrcode was made recently, and by tightening the allowed time difference between system and the qrcode, sending qrcodes online to scan can be made nearly impossible. Finally the airgapped laptop cannot install programs, so my solution was to write it all in VBA so the excel would work like a database and the input box built into excel would accept the scanner text input.(The duty person would open the excel up for scanning whenever cadets started booking in).

Total time writing this is likely 40 hours, to write this had to learn basic app creation with kivy and swift from scratch, also some VBA too. Because I will never use a mac, had to code swift on my mom's ipad.
The following images are the login page(after inserting 4d already)
<br />
<p align="center">
<img src="https://github.com/user-attachments/assets/5fe7269c-14fc-4f8d-8d98-d4027829a50d">
</p>
<br />
And two images to show how it changes with time.
<br />
<p align="center">
<img src="https://github.com/user-attachments/assets/e8b53d9a-1b07-4300-9f26-24ccddcccfae">
<img src="https://github.com/user-attachments/assets/6691b0a9-1474-4254-8a9d-245cca70c7fb">
</p>
