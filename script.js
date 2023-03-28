let bgColorList = [
    "#0072C6",
    "#D4145A",
    "#00A398",
    "#FF5800",
    "#444444"
  ];
  
  let bgIndex = 0;
  
  setInterval(() => {
    document.body.style.backgroundColor = bgColorList[bgIndex];
    bgIndex = (bgIndex + 1) % bgColorList.length;
  }, 2000);
  