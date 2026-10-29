let sidebarOpener;

document.getElementById("mySidebar").inert = true;

function openNav(opener = document.querySelector(".openbtn")) {
  const sidebar = document.getElementById("mySidebar");
  sidebarOpener = opener;
  sidebar.inert = false;
  sidebar.style.width = "100%";
  sidebarOpener.setAttribute("aria-expanded", "true");
  sidebar.querySelector(".closebtn").focus();
}

function closeNav() {
  const sidebar = document.getElementById("mySidebar");
  sidebar.style.width = "0";
  if (sidebarOpener) {
    sidebarOpener.setAttribute("aria-expanded", "false");
    sidebarOpener.focus();
  }
  sidebar.inert = true;
}
