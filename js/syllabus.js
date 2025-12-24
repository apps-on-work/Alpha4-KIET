  const notesData = {
    FI: {
      calc: ["CFE Syllabus.pdf"],
      phy: ["SPD Syllabus.pdf"],
      dstl: ["DSTL Syllabus.pdf"
      ],
      pps: ["PPS C Syllabus.pdf", "PPS  Python Syllabus.pdf"
      ],
      iot: ["IoT Syllabus.pdf"], 
      cold: ["COLD Syllabus.pdf"]
    },
    SE: {
      phy: ["SPD Syllabus.pdf"]
    },
    TH: {
      java: ["JAVA Syllabus.pdf"]
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
    eee: "EEE",
    java: "JAVA"
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