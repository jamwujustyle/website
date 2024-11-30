function delete_task(taskId) {
  fetch("/delete_task", {
    method: "POST",
    body: JSON.stringify({ taskId: taskId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
