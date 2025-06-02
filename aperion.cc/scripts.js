function updateCompleteStatus(carId, isChecked) {
  fetch("/update_complete", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: carId, complete: isChecked ? 1 : 0 })
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        console.log("Complete status updated.");
      } else {
        console.error("Failed to update complete status.");
      }
    });
}

function updateField(carId, field, value) {
  fetch("/update_field", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: carId, field: field, value: value })
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        console.log(field + " updated!");
      } else {
        console.error("Failed to update " + field + ".");
      }
    });
}
