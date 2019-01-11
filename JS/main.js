function isKid(age) {
	let returnvalue = 9 < age && age < 19;
	return returnvalue;
}

function isAdult(age) {
	let returnvalue = 17 < age && age < 65;
	return returnvalue;
}

function isSenior(age) {
	let returnvalue = 9 < age;
	return returnvalue;
}

function isMale(gender) {
	let returnvalue = gender == "m";
	return returnvalue;
}

function isFemale(gender) {
	let returnvalue = gender == "f";
	return returnvalue;
}

function intToTime(integerTime) {
	let returnvalue = integerTime + ":00";
	return returnvalue;
}

function timeToMinutes(time) {
	let returnvalue;
	if (time.length == 5) {
		returnvalue = parseInt(time.slice(0, 2)) * 60 + parseInt(time.slice(3, 5))
	} else {
		returnvalue = parseInt(time.slice(0)) * 60 + parseInt(time.slice(2, 4))
	}
	return returnvalue;
}

function minutesToTime(minutes) {
	extraMinutes = minutes % 60;
	extraHours = (minutes - extraMinutes) / 60

	if (extraMinutes == 0) {
		return extraHours + ":" + extraMinutes + "0";
	} else if (extraMinutes < 10) {
		return extraHours + ":" + "0" + extraMinutes;
	}
	return extraHours + ":" + extraMinutes;
}

function addTime(time1, time2) {
	let min1 = timeToMinutes(time1);
	let min2 = timeToMinutes(time2);

	min1 /= 60;
	min2 /= 60;

	let minSum = (min1 + min2) % 24;

	minSum *= 60;

	return minSum;
}

function subTime(time1, time2) {
	let min1 = timeToMinutes(time1);
	let min2 = timeToMinuets(time2);

	min1 /= 60;
	min2 /= 60;

	let minDif = (min1 - min2) % 24;

	minDif *= 60;

	return minDif;
}

function findHours(time) {
	if (time.length() == 5) {
		return time.slice(0, 2);
	}

	return time.slice(0);
}

//code begins

function storeGender(gender) {
	if (gender == "m") {
		localStorage.setItem("gender", "m");
	} else {
		localStorage.setItem("gender", "f");
	}
	window.location.href = "age.html";
}

function storeAge() {
	let age = document.getElementById("name");
	localStorage.setItem("age", age);
	window.location.href = "wakeTime.html";
}

//finish other js stuff

function storeWakeTime() {
	let waketime = document.getElementById("name");
	localStorage.setItem("waketime", waketime);
    window.location.href = "bedtime.html";
}

var sleepTimesList = [];

function timesCalc() {
	let age = localStorage.getItem("age");
	let wakeTime = localStorage.getItem("waketime");
	let gender = localStorage.getItem("gender");
		
		if (isKid(age)) {
			let kidWakeTime = subTime(wakeTime, "3:00");

		for (i = 0; i < 6; i++) {
			let kidMinutes = minutesToTime(90 * (i + 1));
			let kidSleep = subTime(kidWakeTime, kidMinutes);

			if (isFemale(gender)) {
				kidSleep = subTime(kidSleep, "0:20");
			}

			sleepTimesList.push(kidSleep);
		}
	}

	else if (isAdult(age)) {
		for (i = 0; i < 6; i++) {
			let adultMinutes = minutesToTIme(90 * (i + 1));
			let adultSleep =  subTime(wakeTime, adultMinutes);

			if (isFemale(gender)) {
				adultSleep = subTime(adultSleep, "0:20");
			}
			
			sleepTimesList.push(adultSleep);
		}
	}

	else if (isSenior(age)) {
		let seniorWakeTime = addTime(wakeTime, "0:30");

		for (i = 0; i < 6; i++) {
			let seniorMinutes = minutesToTime(90 * (i + 1));
			let seniorSleep = subTime(seniorWakeTime, adultMinutes);

			if (isFemale(gender)) {
				seniorSleep = subTime(seniorSleep, "0:20");
			}

			sleepTimesList.push(seniorSleep);
		}
    }
    document.getElementById("choice1").innerHTML = sleepTimesList.slice(0);
    document.getElementById("choice2").innerHTML = sleepTimesList.slice(1);
    document.getElementById("choice3").innerHTML = sleepTimesList.slice(2);
    document.getElementById("choice4").innerHTML = sleepTimesList.slice(3);
    document.getElementById("choice5").innerHTML = sleepTimesList.slice(4);
    document.getElementById("choice6").innerHTML = sleepTimesList.slice(5);
    console.log(sleepTimesList.slice(0));
}

function bedTimeChoice(choice) {
	sleepTimeChoice = sleepTimeList.slice(choice - 1);
	localStorage.setItem("choice", choice);
	return sleepTimeChoice;
}

function happiness(rating) {
	let choice = localStorage.getItem("choice");
	if (rating < 3) {
		let sleepTimeMultiplier = 3 - rating;
		let multiplierTime = minutesToTime(sleepTimmeMultiplier * 44);
		let realSleepTime = subTime(bedTimeChoice(choice), multiplierTime);
	}

	else {
		let realSleepTime = bedTimeChoice(choice);
	}
}

function finalBedtime(realSleepTime, choice) {
	let sleepTime = subTime(realSleepTime, "0:07");
	sleepTime = subTime(sleepTime, "0:30");

	if (sleepTime == choice) {
		return "Perfect! Tonight, you can sleep at " + sleepTime;
	}
	else {
		return "Tonight, try to sleep at " + sleepTime;
	}
}