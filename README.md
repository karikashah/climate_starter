# climate_starter

For this project there are 2 steps:
1. ## Climate Analysis & Exploration
  a. You can view the **source code** at **<em>climate_starter.ipynb</em>** <br>
  b. For graphs <br>
  Precipitation Analysis <br>
  ![Precipitation Analysis](https://github.com/karikashah/climate_starter/blob/master/Output/Precipitation_last_12months.png)
  
  --------------------------
  Station Analysis <br>
  ![Station Analysis](https://github.com/karikashah/climate_starter/blob/master/Output/Temperature_for_active%20station_last_12months.png)
  
  --------------------------
  Temperature Analysis <br>
  ![Temperature Analysis](https://github.com/karikashah/climate_starter/blob/master/Output/Bar_MyTrip_Avg_Temp.png)
  
  --------------------------
  Predicated Temperature Analysis <br>
  ![Predicated Temperature Analysis](https://github.com/karikashah/climate_starter/blob/master/Output/Predicted_Temperatures_for_Trip.png)
  
  --------------------------
 2. ## Climate app
   Use of Flask & SQLAlchemy to create different routes for the above generated graphs. <br>
   a. Following routes were created:<br>
        / <br>
        /api/v1.0/precipitation <br>
        /api/v1.0/stations <br>
        /api/v1.0/tobs <br>
        /api/v1.0/`<start>` <br>
        /api/v1.0/`<start>`/`<end>` <br>
   b. You can view the **source code** at **<em>climate_app.py</em>**
