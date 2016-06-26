var config = {
		apiKey: "AIzaSyDtOHC7eGyxagcDxLCzRNzJRn1-RXp60JE",
		authDomain: "project-1-dc0ac.firebaseapp.com",
		databaseURL: "https://project-1-dc0ac.firebaseio.com",
		storageBucket: "project-1-dc0ac.appspot.com",
		};
firebase.initializeApp(config);




var database = firebase.database();
window.onload = function() {
	database.ref("global_click_counter").on('value', function(dataSnapshot) {
			var counter = dataSnapshot.val();
			document.getElementById("counter_value").innerHTML = counter;
		});
	document.getElementById("counter_button").onclick = function() {
			database.ref("global_click_counter").once('value').then(function(dataSnapshot) {
				var counter = dataSnapshot.val();
				database.ref("global_click_counter").set(counter + 1);
				//document.getElementById("counter_value").innerHTML = counter;
			}, function (err) {
				console.log(err);
			});
		};
}