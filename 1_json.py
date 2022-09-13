import json


# structural representation of the department within the faculty of KRSU
some_requested_data = {

	"department1": {
		"name": "Department of Applied Mathematics and Informatics",
		"head": "Borubaev Altai Aslannovich",

		"additional_info": {
			"phone number": 123123123,
			"mail": "mail@gmail.com",
			"web-site": "http://epm.krsu.edu.kg/",
		},
		
		"teaching_staff": [
			{
				"name": "Borubaev Altai Aslannovich",
				"Degree, position": "Head of the Department of Applied Mathematics and Informatics, Doctor of Physical and Mathematical Sciences, Professor, Academician of the National Academy of Sciences of the Kyrgyz Republic"
			},
			{
				"name": "Doulbekova Saltanat Baiyzbekovna",
				"Degree, position": "Senior Lecturer"
			},
			{
				"name": "Krasnichenko Lyubov Sergeevna",
				"Degree, position": "Associate Professor, Candidate of Physical and Mathematical Sciences"
			},
			{
				"name": "Pankov Pavel Sergeevich",
				"Degree, position": "Professor, Doctor of Physical and Mathematical Sciences, Corresponding Member of the National Academy of Sciences of the Kyrgyz Republic"
			}
		]
	}

}


# as variable
y = json.dumps(some_requested_data)


# as file
with open("data_file.json", "w") as write_file:
    json.dump(some_requested_data, write_file)
