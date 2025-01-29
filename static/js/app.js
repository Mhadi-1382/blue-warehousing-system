
/*!
 * BLUE (Warehousing System) Template
 * Created on date: 1403/06/20
 *
 * View source code on GitHub: https://github.com/Mhadi-1382/
*/

// Navbar
var asideRightOverlayNavbar = document.querySelector(".aside-right-overlay");
function asideRightOverlayNavbarFunc() {
    asideRightOverlayNavbar.classList.toggle("navbar-toggle");
}

// Check status internet
var internetStatusModalMessage = document.querySelector("#modalStatusInternet .modal-header");
var internetStatusChecking = document.getElementById("internetStatusChecking");
var internetStatusOnline = document.getElementById("internetStatusOnline");
var internetStatusOffline = document.getElementById("internetStatusOffline");
window.addEventListener("load", function() {
    if (navigator.onLine) {
        setTimeout(() => {
            internetStatusChecking.style.display = "none";
            internetStatusOffline.style.display = "none";
            internetStatusOnline.style.display = "flex";

            internetStatusModalMessage.innerHTML = `
            <h4>اتصال برقرار است 👋</h4>
            <p>دسترسی شما برای دریافت اطلاعات جدید از ابر برقرار است.</p>
            `;
        }, 1000)
    } else {
        setTimeout(() => {
            internetStatusChecking.style.display = "none";
            internetStatusOffline.style.display = "flex";
            internetStatusOnline.style.display = "none";

            internetStatusModalMessage.innerHTML = `
            <h4>خطای اتصال!</h4>
            <p>لطفا اتصال خود را بررسی و دوباره امتحان کنید.</p>
            `;
        }, 1000)
    }
})

// Modals
var modalStatusInternet = document.getElementById("modalStatusInternet");
function modalStatusInternetFunc() {
    modalStatusInternet.classList.toggle("modal-toggle");
}
var modalAddUserManager = document.getElementById("modalAddUserManager");
function modalAddUserManagerFunc() {
    modalAddUserManager.classList.toggle("modal-toggle");
}

// Alerts
var alertError = document.getElementById("alertError");
var alertInfo = document.getElementById("alertInfo");
var alertWarning = document.getElementById("alertWarning");
var alertMessage = document.getElementById("alertMessage");
setTimeout(() => {
    alertError.classList.add("alert-toggle");
}, 5000);
setTimeout(() => {
    alertInfo.classList.add("alert-toggle");
}, 5000);
setTimeout(() => {
    alertWarning.classList.add("alert-toggle");
}, 5000);
setTimeout(() => {
    alertMessage.classList.add("alert-toggle");
}, 5000);

// Form control
let inputSubmitChangeStatus = document.getElementById("inputSubmit");
inputSubmitChangeStatus.onclick = function() {
    inputSubmitChangeStatus.value = `در حال بررسی...`;
    setTimeout(() => {
        inputSubmitChangeStatus.value = `ورود`;
    }, 5000);
}
