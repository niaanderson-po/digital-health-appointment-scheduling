Architectural Design-

User Scenerio:

There is already a service for reserving a doctor's appointment, but there is a need for additional services to book appointments with psychiatrists and nutritionists.

Architectural Design Explanation:

No architectural changes are needed here. Booking and availability doesn’t differ between different types of specialists. The same structure works for them all. A better name for ‘book doctor’ could be something more general, for example ‘book appointment’.

User Scenerio:

In the currect architectural design the patient UI and personnel UI are depicted seprate, in different boxes, even though they have similarities like requiring access to the details of a scheduled appointment.

Architectural Design Explanation:

They are kept separated, as this is more user friendly. Patients and personnel could use the same user interface, but both would see functionality they would never need (ie booking an appointment vs adding an appointment slot). However, having a different view for each type of user helps to design clear user interfaces, where only necessary functionality is included for each user.

User Scenerio:

Digital Health wants to integrate with a partner hospital. The integration would be used for getting patient records once a day.

Architectural Design Explanation:

A timer launches automatically sending a request from External Data Service of Digital Health to External Data Service of the partner hospital. The partner hospital responds with the latest changes in patient records on this request. This information is stored in Digital Health’s patient records database. This way Digital Health doesn’t have to know how data is stored at the partner hospital. They only need to know what kind of request to send to them and the data format to expect on their response.

This is more ideal than the External Data Service of the partner hospital sending data from their External Data Service on agreed intervals where the data is exported from the partner hospital's database and imported to a corresponding Digital Health database. This would unfavorably require the databases to have an identical structure.

A possible challenege with the preferred partner hospital integration, however, relates to the data transferring every day, even if there is not immediate need for all of the data. This is a potential problem and needs closer analysis because the data here is personal data, and there must always be a proper reason for transferring and storing it, and approvals are needed from the patients themselves.
