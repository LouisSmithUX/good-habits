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

  // var to_delete = document.querySelectorAll("[data_id='"+habit_id.toString()+"']");
  // to_delete.forEach(function(item,index){item.parentNode.removeChild(item);});

  location.reload();

  return true;
};

document.addEventListener("DOMContentLoaded", function(){ 

  var new_habit = document.getElementById('new_habit');
  var delete_habit_buttons = document.getElementsByClassName('delete_habit');
  var modal_bg = document.getElementsByClassName("modal_bg")[0];
  var modal = document.getElementById('modal');
  var create_habit_modal = document.getElementById('create_habit_modal');
  var delete_habit_modal = document.getElementById('delete_habit_modal');
  var confirm_delete = document.getElementById('confirm_delete');
  var cancel_delete = document.getElementById('cancel_delete');

  function hide_modals() {
      modal.style.display = 'none';
      create_habit_modal.style.display = 'none';
      delete_habit_modal.style.display = 'none';
  };

  modal_bg.onclick = function(event) { hide_modals(); };
  cancel_delete.onclick = function(event) { hide_modals(); };


  new_habit.onclick = function(event) {
    modal.style.display = 'block';
    create_habit_modal.style.display = 'block';
  };

  for (let delete_habit_button of delete_habit_buttons) {
   delete_habit_button.onclick = function(event) {
      modal.style.display = 'block';
      delete_habit_modal.style.display = 'block';
      confirm_delete.setAttribute('data_id',event.target.closest('.habit').getAttribute('data_id'));
    };
  };

  confirm_delete.onclick = function(event) { 
    hide_modals();
    deleteHabit(caller=event.target, habit_id=event.target.getAttribute('data_id'));
  };
});
