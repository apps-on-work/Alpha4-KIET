  const notesData = {
    FI: {
      calc: ["CFE Unit 1.pdf", "CFE Unit 2.pdf", "CFE Unit 3.pdf", "CFE Unit 4.pdf", "CFE Unit 5.pdf"],
      phy: ["SPD Unit 1.pdf", "SPD Unit 2.pdf", "SPD Unit 3.pdf", "SPD Unit 4.pdf", "SPD Unit 5.pdf"],
      dstl: ["DSTL Unit 1.pdf", "DSTL Unit 2.pdf", "DSTL Unit 3.pdf", "DSTL Unit 4.pdf", "DSTL Unit 5 Part 1.pdf",
        "DSTL Unit 5 Part 2.pdf"
      ],
      pps: ["PPS C Unit 1.pdf", "PPS  C Unit 2.pdf", "PPS C Unit 3.pdf", "PPS C Unit 4.pdf", "PPS C Unit 5.pdf",
        "PPS Python Unit 1.pdf", "PPS Python Unit 2.pdf", "PPS Python Unit 3.pdf", "PPS Python Unit 4.pdf", "PPS Python Unit 5.pdf"
      ],
      iot: ["IoT Sensors.pdf", "IoT Arduino Uno.pdf", "IoT ESP8266.pdf"], 
      cold: ["COLD Super.pdf"]
    },
    SE: {
      phy: ["SPD Unit 5.pdf", "Semiinsulator Unit 2.pdf"]
    },
    TH: {
      // no subjects yet
    },
    FH: {
      // no subjects yet
    }
  };

  const subjectNames = {
    calc: "CFE",
    phy: "SPD",
    dstl: "DSTL",
    pps: "PPS", 
    iot: "IoT", 
    cold: "COLD",
    chem: "EC",
    dnr: "DnR",
    eee: "EEE"
  };

  const yearSelect = document.getElementById("year");
  const subjectSelect = document.getElementById("subject");
  const pdfList = document.getElementById("pdfList");

  subjectSelect.disabled = true;

  yearSelect.addEventListener("change", () => {
    const year = yearSelect.value;

    pdfList.innerHTML = "";
    subjectSelect.innerHTML = `<option value="">--Select Subject--</option>`;

    if (!year || !notesData[year] || Object.keys(notesData[year]).length === 0) {
      subjectSelect.disabled = true;
      return;
    }

    Object.keys(notesData[year]).forEach(subjectKey => {
      const option = document.createElement("option");
      option.value = subjectKey;
      option.textContent = subjectNames[subjectKey] || subjectKey;
      subjectSelect.appendChild(option);
    });

    subjectSelect.disabled = false;
  });

  subjectSelect.addEventListener("change", () => {
    const year = yearSelect.value;
    const subject = subjectSelect.value;

    pdfList.innerHTML = "";

    if (year && subject && notesData[year][subject]) {
      notesData[year][subject].forEach(pdf => {
        const link = document.createElement("a");
        link.href = `notes/${year}/${pdf}`;
        link.target = "_blank";
        link.textContent = pdf;
        pdfList.appendChild(link);
      });
    }
  });
