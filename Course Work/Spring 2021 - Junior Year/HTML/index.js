let tasks = [
  {
    id: 0,
    title: "Doing Laundary",
    dueDate: new Date(2020, 1, 28),
    completed: false,
    completeDate: null,
    createdDate: new Date(2020, 1, 23),
    deleted: false,
    note: "I need to get quarters first at Kroger."
  },
  {
    id: 1,
    title: "CS3744 Assignment 3",
    dueDate: new Date(2020, 2, 17),
    completed: false,
    completeDate: null,
    createdDate: new Date(2020, 1, 24),
    deleted: false,
    note: "I better start early cuz it looks pretty complicated.\r\nLooks like I have to read w3schools.com a lot."
  },
  {
    id: 2,
    title: "Getting AAA batteries",
    dueDate: null,
    completed: true,
    completeDate: new Date(2020, 2, 1),
    createdDate: new Date(2020, 1, 26),
    deleted: false,
    note: "for my remote control."
  },
  {
    id: 3,
    title: "Booking a flight ticket ACM CHI conference",
    dueDate: new Date(2020, 3, 15),
    completed: false,
    completeDate: null,
    createdDate: new Date(2020, 2, 26),
    deleted: false,
    note: "I would have to book a flight ticket to ACM CHI conference.\r\nKeep an eye on the cancellation policy. the conference may be cancelled due to the cornoa virus outbreak. :( Although flight tickets are getting cheaper."
  }
];

var overdueOn = false;
var hideCompletedOn = false;

let = addTask = function () {
  if ($('#task-title').val() == "") {
    alert("Task title is required");
  }
  else {

    var taskTitle = $('#task-title').val();
    var due = $('#due-date').val();
    var taskNote = $('#task-note').val().replace(/\r\n|\r|\n/g, "<br />");

    if (due == "") {
      tasks[tasks.length] = {
        id: tasks.length,
        title: taskTitle,
        dueDate: null,
        completed: false,
        completeDate: null,
        createdDate: new Date(),
        deleted: false,
        note: taskNote
      };
      $("#myModal").modal('hide');
      $("#myModal").find('form').trigger('reset');

      render();
    }
    else if (isNaN(Date.parse(due))) {
      alert("Check your date format.");
    } else {
      var mm = due.slice(0, 2);
      var dd = due.slice(3, 5);
      var yyyy = due.slice(6, 10);
      tasks[tasks.length] = {
        id: tasks.length,
        title: taskTitle,
        dueDate: new Date(yyyy, mm - 1, dd),
        completed: false,
        completeDate: null,
        createdDate: new Date(),
        deleted: false,
        note: taskNote
      };
      $("#myModal").modal('hide');
      $("#myModal").find('form').trigger('reset');

      render();
    }

  }
}

let render = function () {

  var i
  var d1;
  var m1;
  var y1;
  var r1;
  var d2;
  var m2;
  var y2;
  var r2;
  var checked;
  var currentDate = new Date();
  var title = [""];
  var numComplete = 0;

  for (i = 0; i < tasks.length; i++) {
    // console.log('#' + tasks[i].id);
    $('#' + tasks[i].id).remove();
    $('#note-' + tasks[i].id).remove();
  }



  for (i = 0; i < tasks.length; i++) {

    if (!tasks[i].deleted) {

      if (tasks[i].title.length > 30) {
        title[i] = tasks[i].title.slice(0, 30) + '...';
      }
      else {
        title[i] = tasks[i].title;
      }

      $("#tasks").append("<tr id='" + tasks[i].id + "'></tr>");
      if (tasks[i].completed) {
        $("#" + tasks[i].id).addClass('success');
        title[i] = ('<del>' + title[i] + '</del>');
        if (tasks[i].completeDate === null) {
          tasks[i].completeDate = currentDate;
        }
        checked = ' checked=""';
        numComplete += 1;
      }
      else {
        tasks[i].completeDate = null;
        checked = '';
      }

      if (String(tasks[i].dueDate) === "null") {
        r1 = "";
      } else {
        d1 = tasks[i].dueDate.getDate();
        if (d1 < 10) {
          d1 = '0' + d1;
        }
        m1 = tasks[i].dueDate.getMonth();
        m1 += 1;
        if (m1 < 10) {
          m1 = '0' + m1;
        }
        y1 = tasks[i].dueDate.getFullYear();
        r1 = m1 + '/' + d1 + '/' + y1;
      }

      if (String(tasks[i].completeDate) === "null") {
        r2 = "";
      } else {
        d2 = tasks[i].completeDate.getDate();
        if (d2 < 10) {
          d2 = '0' + d2;
        }
        m2 = tasks[i].completeDate.getMonth();
        m2 += 1;
        if (m2 < 10) {
          m2 = '0' + m2;
        }
        y2 = tasks[i].completeDate.getFullYear();
        r2 = m2 + '/' + d2 + '/' + y2;
      }

      $("#" + tasks[i].id).append('<td class="text-center"><input type="checkbox" class="form-check-input" value="' + tasks[i].id + '"' + checked + '></td><td class="text-center">' + title[i] + '</td><td class="text-center"><span class="text-right"><button class="btn btn-xs btn-warning" data-toggle="collapse" data-target="#note-' + tasks[i].id + '"><span class="glyphicon glyphicon-triangle-bottom"> </span> Note</button></span></td><td class="text-center">' + r1 + '</td><td class="text-center">' + r2 + '</td><td class="text-center"> <button type="button" class="btn btn-danger btn-xs deletetask" alt="Delete the task" value="' + tasks[i].id + '"><span class="glyphicon glyphicon-trash"></span></button> <a target="_blank" href="mailto:?body=' + tasks[i].note.replace(/\r\n|\r|\n/g, "<br />") + '&amp;subject=' + tasks[i].title + '"><button type="button" class="btn btn-danger btn-xs emailtask" alt="Send an email" value="' + tasks[i].id + '"><span class="glyphicon glyphicon-envelope"></span></button></a> </td>');
      $("#tasks").append("<tr id='note-" + tasks[i].id + "'  class='collapse'></tr>");
      $("#note-" + tasks[i].id).append('<td></td> <td colspan="5"> <div class="well"> <h3>' + tasks[i].title + '</h3> <div>' + tasks[i].note.replace(/\r\n|\r|\n/g, "<br />") + '</div> </div> </td>');

      if (tasks[i].dueDate < currentDate && !$("#" + tasks[i].id).hasClass("success") && tasks[i].dueDate !== null) {
        $("#" + tasks[i].id).addClass('danger');
      }
    }
  }

  if (numComplete == 0) {
    $('#deleteCompletedTasks').replaceWith('<button type="button" class="btn btn-danger" id="deleteCompletedTasks" disabled><span class="glyphicon glyphicon-trash"></span>&nbsp; Delete Completed Tasks</button>');
  } else {
    $('#deleteCompletedTasks').replaceWith('<button type="button" class="btn btn-danger" id="deleteCompletedTasks"><span class="glyphicon glyphicon-trash"></span>&nbsp; Delete Completed Tasks</button>');
  }

  if (overdueOn) {
    for (i = 0; i < tasks.length; i++) {
      if (!$('#' + i).hasClass("danger")) {
        $('#' + i).fadeOut(0);
      }
    }
  }

  if (hideCompletedOn) {
    for (i = 0; i < tasks.length; i++) {
      if ($('#' + i).hasClass("success")) {
        $('#' + i).fadeOut(0);
      }
    }
  }

  var z = document.getElementsByClassName("form-check-input");
  for (var i = 0; i < z.length; i++) {
    z[i].addEventListener("click", function () {

      if (this.checked) {
        tasks[this.value].completed = true;
      }
      else {
        tasks[this.value].completed = false;
        numComplete -= 1;
      }

      render();
    });
  }

  var x = document.getElementsByClassName("btn btn-danger btn-xs deletetask");
  for (var i = 0; i < x.length; i++) {
    x[i].addEventListener("click", function () {
      var entry = confirm("Are you sure you want to delete this task?");
      if (entry == true) {
        if (tasks[this.value].completed) {
          numComplete -= 1;
        }
        tasks[this.value].deleted = true;
        render();
      }
    });
  }

  document.getElementById("deleteCompletedTasks").addEventListener("click", function () {
    if (numComplete == 1) {
      var entry = confirm("Do you want to delete 1 task?");
    } else {
      var entry = confirm("Do you want to delete " + numComplete + " tasks?");
    }
    if (entry == true) {
      var j;
      for (j = 0; j < tasks.length; j++) {
        if (tasks[j].completed && !tasks[j].deleted) {
          tasks[j].deleted = true;
          numComplete -= 1;
        }
      }
      render();
    }
  });

  document.getElementsByClassName("btn btn-success addtask")[0].addEventListener("click", function () {
    $("#myModal").modal();
  });

  document.getElementsByClassName("btn btn-success btn-default pull-left")[0].setAttribute('type', 'button');
  document.getElementsByClassName("btn btn-success btn-default pull-left")[0].addEventListener("click", addTask);


}




$(document).ready(function () {

  render();

  $('#overdue').on('click', function () {

    if (overdueOn) {
      overdueOn = false;
      $('#overdue').removeClass("active");
    } else {
      overdueOn = true;
      $('#overdue').addClass("active");
    }

    render();

  })

  $('#hidecompleted').on('click', function () {

    if (hideCompletedOn) {
      hideCompletedOn = false;
      $('#hidecompleted').removeClass("active");
    } else {
      hideCompletedOn = true;
      $('#hidecompleted').addClass("active");
    }

    render();

  })

})