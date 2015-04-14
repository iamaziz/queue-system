
### Software implementation (Related resources and background)

**theory:**
- Paper:
	- Using Compartmental Models to Predict Hospital Bed Occupancy, [pdf](http://www.researchgate.net/publication/228850639_Using_Compartmental_Models_to_Predict_Hospital_Bed_Occupancy)
	- Physicians' Ability to Predict Hospital Length of Stay for Patients Admitted to the Hospital from the Emergency Department, [pdf](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3272796/)
- [A Design for Evidence-based Software Architecture Research](http://users.ece.utexas.edu/~perry/work/papers/R2A-05-Evidence.pdf)

- The Evidence for Evidence-Based Design, [ppt](http://www.aia.org/aiaucmp/groups/aia/documents/pdf/aiab091011.pdf)

- Articles:
	- [10 Medical Practice Management Systems For 2014](http://www.informationweek.com/healthcare/electronic-health-records/10-medical-practice-management-systems-for-2014/d/d-id/1252791?itc=edit%5Fin%5Fbody%5Fcross&image_number=2)

	- [Designers, take a look at evidence-based design for health care](http://www.fastcodesign.com/1418953/designers-take-a-look-at-evidence-based-design-for-health-care)


**software:**

- [Patient Management Software (PMS)](https://en.wikipedia.org/wiki/Patient_management_software)
- [Medical Practice Management Software](https://en.wikipedia.org/wiki/Medical_practice_management_software)
- [List of open source health software](https://en.wikipedia.org/wiki/List_of_open-source_health_software)
- [Health care process management in python: Use Case](http://publications.crs4.it/pubdocs/2011/Cab11/healthcare-process-management-in-python-a-use-case.pdf)



*implemented (open source) applications*

- [GNUmed](http://wiki.gnumed.de/bin/view/Gnumed/InstallerGuideHomeShort), python
	- To launch `GNUmed Client` from source, run:

	    $ `./external-tools/check-prerequisites.sh`

	    to verify dependencies, then (if all good)

	    $ `python client/gnumed.py`


- [OpenMolar2](https://openmolar.com/om2), python

	- [documentations](https://static.openmolar.com/om2/documentation/current/contents.html)

To run Openmolar2 from source (currently installed at the project directory `~/Desktop/projects/pace-gupta/src/openmolar2` ):

	$ python src/main.py

	or
	$ python src/server.py --start
	then:
	$ python src/client.py

	- Installing dependencies (PyQt4, MySQL, Qsci, ... etc) and configuration took about +6 hours.

	- Issues:

		- regular launching method does not work yet, to launch manually
		go to
		$ cd /Library/Python/2.7/site-packages/openmolar
		then
		$ python main.py

			database passwd: EMPTY
			user: root pswd: toor


*options for creating application from scratch*

- [Kivy](http://kivy.org/)


<hr>
