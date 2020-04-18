// Example POST method implementation:
async function toggleCompletion(caller, date = '', habit = '') {
  // Default options are marked with *

  var url = '/habit_event/new';

  var data = {date: date, habit: habit};

  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *client
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });

  response.json().then(function(parsedJson) {

    if (parsedJson.age>19) {
      caller.className = '';
      caller.classList.add('level6', 'row', 'today');
    } else if (parsedJson.age>11) {
      caller.className = '';
      caller.classList.add('level5', 'row', 'today');
    } else if (parsedJson.age>6) {
      caller.className = '';
      caller.classList.add('level4', 'row', 'today');
    } else if (parsedJson.age>3) {
      caller.className = '';
      caller.classList.add('level3', 'row', 'today');
    } else if (parsedJson.age>1) {
      caller.className = '';
      caller.classList.add('level2', 'row', 'today');
    } else if (parsedJson.age==1) {
      caller.className = '';
      caller.classList.add('level1', 'row', 'today');
    } else {
      caller.className = '';
      caller.classList.add('row');
    }
  });

  return true; // parses JSON response into native JavaScript objects
}

async function deleteHabit(caller, habit_id) {
  var url = '/habit/delete';

  var data = {habit_id: habit_id};

  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *client
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });

  var to_delete = document.querySelectorAll("[data_id='"+habit_id.toString()+"']");
  to_delete.forEach(function(item,index){item.parentNode.removeChild(item);});

  return true;
};

document.addEventListener("DOMContentLoaded", function(){ 

  var new_habit = document.getElementsByClassName('new_habit')[0];
  var body = document.getElementsByTagName("body")[0];
  var modal = document.getElementById('modal');


  body.onclick = function(event) {
    if (!event.target.closest('#modal .card') && event.target!=new_habit) {
      modal.style.display = 'none';
// console.log('sdf');    
};
  };

  new_habit.onclick = function(event) {
    modal.style.display = 'block';
  };
});