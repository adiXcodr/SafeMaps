<h1 align="center" >SAFE MAPS</h1>
<h3 align="center"> A Web App made for safe navigation during a Pandemic</h3>

## Technologies used
* Python
* networkx
* flask
* HTML, CSS

### Demo
https://safemaps.herokuapp.com/

### Project Structure
This project has three major parts :
1. app.py - This contains Flask APIs that receives movie a review through GUI or API calls, computes the precited value based on our model and returns it.
2. index.html - The HTML template to allow user to enter the movie review.

### Steps to run the application

1. Run app.py using the command below to start Flask API
```
python app.py
```
   
2. Navigate to URL http://localhost:5000

3. To close the server, press Ctrl+C 

<br>

### Terms

We will use some parameters as follows:

1. Density of people affected (DPA) on each edge between two nodes [people affected/length of path]
2. Traffic Intensity Level (TIL)
3. Crime Rate Level (CRL)
4. Distance between two nodes (DIS)

### Plan

1. Create a network of places in a city and make a connected graph of say ‘n’ predefined places.
2. Assign the number of people and number of people infected to each edge.
3. Assign TIL, CRL and DIS to each edge randomly.
4. Assign the Distance to each edge randomly.
5. We make an interface between the user and the computer using a suitable UI platform. The user will select the source and destination from the given places.
6. Find all possible paths between the two nodes and find the paths for which the sum of DPA is less.
7. If there are multiple paths for which the difference in DPA is negligible (<=5), then look for the time in system clock.
8. If it’s Night time, then look for the paths in which crime less and if it’s daytime then look for the paths in which TIL is less.
9. Till now we might have achieved a single path or few paths in
which the difference between DPA and the difference between TIL (<=2) or the difference between CRL (<=1) is negligible.
10. Among the paths obtained, find the path with minimum distance (DIS)
11. The path obtained will be our output.

### Author

#### [Adittya Dey](https://github.com/adiXcodr)

[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/adittya-dey-3966b916b/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/adittya.dey.3)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/adixdey/)


#### [Abhinav Anand](https://github.com/abhinavanandthakur)

[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/abhinav-anand-1a3510194)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/profile.php?id=100024901720234)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/abhinav_a_thakur/)

