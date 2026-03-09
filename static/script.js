// Initialize months array
function generateMonths() {
    let start = new Date(2022, 8, 1);
    let end = new Date(2026, 2, 1);
    let months = [];

    while (start <= end) {
        let y = start.getFullYear();
        let m = (start.getMonth() + 1).toString().padStart(2, '0');
        months.push(`${y}-${m}`);
        start.setMonth(start.getMonth() + 1);
    }
    return months;
}

let months = generateMonths();

// Fill salary from start month
function fillFromStart() {
    let salary = parseFloat(document.getElementById("start_salary").value);
    
    if (!salary || isNaN(salary) || salary <= 0) {
        alert("Please enter a valid starting salary");
        return;
    }

    // Show salary grid
    document.getElementById("salary_section").style.display = "block";

    // Fill all months
    for (let i = 0; i < months.length; i++) {
        let id = months[i];
        let field = document.getElementById(id);
        
        if (!field) continue;
        
        let month = parseInt(id.split("-")[1]);
        
        if (month === 9 && id !== "2022-09") {
            salary = Math.round(salary * 1.02);
        }
        
        field.value = salary;
    }

    updateLeaveSurrender();
}

// Recalculate from a specific month
function recalcFrom(monthId) {
    let startIndex = months.indexOf(monthId);
    if (startIndex === -1) return;

    let prevSalary = parseFloat(document.getElementById(monthId).value);
    
    if (!prevSalary || isNaN(prevSalary) || prevSalary <= 0) {
        alert("Please enter a valid salary amount");
        return;
    }

    for (let i = startIndex + 1; i < months.length; i++) {
        let id = months[i];
        let field = document.getElementById(id);
        
        if (!field) continue;
        
        let month = parseInt(id.split("-")[1]);
        
        if (month == 9) {
            prevSalary = Math.round(prevSalary * 1.02);
        }
        
        field.value = prevSalary;
    }

    updateLeaveSurrender();
}

// Update leave surrender fields
function updateLeaveSurrender() {
    let apr2023 = document.getElementById("2023-04");
    let apr2024 = document.getElementById("2024-04");
    let apr2025 = document.getElementById("2025-04");

    if (apr2023 && apr2023.value) {
        document.getElementById("leave_2023").value = apr2023.value;
    }

    if (apr2024 && apr2024.value) {
        document.getElementById("leave_2024").value = apr2024.value;
    }

    if (apr2025 && apr2025.value) {
        document.getElementById("leave_2025").value = apr2025.value;
    }
}

// Clear all fields
function clearAllFields() {
    if (confirm("Are you sure you want to clear all fields?")) {
        // Clear salary fields
        months.forEach(id => {
            let field = document.getElementById(id);
            if (field) field.value = "";
        });
        
        // Clear leave fields
        ["leave_2023", "leave_2024", "leave_2025"].forEach(id => {
            let field = document.getElementById(id);
            if (field) field.value = "";
        });
        
        // Clear start salary
        document.getElementById("start_salary").value = "";
        
        // Hide salary section
        document.getElementById("salary_section").style.display = "none";
    }
}

// Function for fillYear (called from oninput)
function fillYear(element) {
    if (element && element.id) {
        recalcFrom(element.id);
    }
}

// Initialize on document load
document.addEventListener("DOMContentLoaded", function() {
    // Get elements
    let startSalaryInput = document.getElementById("start_salary");
    let calculateBtn = document.querySelector('button[type="submit"]');
    
    // Add input event for start salary
    if (startSalaryInput) {
        startSalaryInput.addEventListener("input", fillFromStart);
    }
    
    // Add input events for all month fields
    months.forEach(function(m) {
        let field = document.getElementById(m);
        if (field) {
            field.addEventListener("input", function() {
                recalcFrom(m);
            });
        }
    });
    
    // Make functions globally available for onclick events
    window.fillFromStart = fillFromStart;
    window.recalcFrom = recalcFrom;
    window.clearAllFields = clearAllFields;
    window.fillYear = fillYear;
});