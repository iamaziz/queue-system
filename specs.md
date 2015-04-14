## Software specs

###Project Implementation

We (Gaynor - Nitish) had discussed that it is simulation of Hospital management system.
Having objectives like:

1. Create a queue for patients (can be multiple queues).
2. Randomly create patients (say requests) and put them in queue
3. Set a response time/serve time for every patient.
4. If there are high number of requests, response time is less and vice-versa.
5. The program must display requests and response time/serve time with randomized rate of increase and decrease of requests (patients).


**Objectives:**

- Minimum response time (to handle patients flow into the hospital).
- Best accommodation.
- Minimum cost.
- Accurately predict rooms availability (in the future).


**Variables:**

- Time
- Patients
- Rooms

**Techniques and Tools**

- Time series analysis.
- Prediction and probability (per Dr. Gaynor).


**Use cases:**

- The User (nurse / hospital staff) enters patients data (check in / check out times).
- The User uses previous data to predict room occupancy and availability.

<hr>

## Design overview

**tools**

- DB: SQLite or PyMongo (MongoDB)
- GUI: Kivy, PyQt, PySide


**potential classes**

```
- Controller (logic/manipulate):

  DataEntry [name, arrival, departure, service time]
  RoomAvailability [currentlyAvailable, reserve, release]
  PatientsHandling [checkIn, checkOut]

- Model (data/db):

- View (presentation - GUI/browser):


```

<hr>
