const colorGroupSelect = document.getElementById('colorGroup');
    const nameTypeDensitySelect = document.getElementById('nameTypeDensity');

    const optionsData = {
      FAOC: [
        "Fair Ocre (FAOC) Solid 10",
        "Fair Ocre (FAOC) Solid 15",
        "Fair Ocre (FAOC) Solid 25",
        "Fair Ocre (FAOC) Solid 35",
        "Fair Ocre (FAOC) Solid 50",
        "Fair Ocre (FAOC) Grad 15",
        "Fair Ocre (FAOC) Grad 25",
        "Fair Ocre (FAOC) Grad 35",
        "Fair Ocre (FAOC) Grad 50",
        "Fair Ocre (FAOC) Double 50 / 20"
      ],
      FABR: [
        "Fair Brown (FABR) Solid 10",
        "Fair Brown (FABR) Solid 15",
        "Fair Brown (FABR) Solid 25",
        "Fair Brown (FABR) Solid 35",
        "Fair Brown (FABR) Solid 50",
        "Fair Brown (FABR) Grad 15",
        "Fair Brown (FABR) Grad 25",
        "Fair Brown (FABR) Grad 35",
        "Fair Brown (FABR) Grad 50",
        "Fair Brown (FABR) Double 50 / 20"
      ],
      FAMN: [
        "Fair Marron (FAMN) Solid 10",
        "Fair Marron (FAMN) Solid 15",
        "Fair Marron (FAMN) Solid 25",
        "Fair Marron (FAMN) Solid 35",
        "Fair Marron (FAMN) Solid 50",
        "Fair Marron (FAMN) Grad 15",
        "Fair Marron (FAMN) Grad 25",
        "Fair Marron (FAMN) Grad 35",
        "Fair Marron (FAMN) Grad 50",
        "Fair Marron (FAMN) Double 50 / 20"
      ],
      GLOR: [
        "Glow Orange (GLOR) Solid 10",
        "Glow Orange (GLOR) Solid 15",
        "Glow Orange (GLOR) Solid 25",
        "Glow Orange (GLOR) Solid 35",
        "Glow Orange (GLOR) Solid 50",
        "Glow Orange (GLOR) Grad 15",
        "Glow Orange (GLOR) Grad 25",
        "Glow Orange (GLOR) Grad 35",
        "Glow Orange (GLOR) Grad 50",
        "Glow Orange (GLOR) Double 50 / 20"
      ],
      GLPL: [
        "Glow Plum (GLPL) Solid 10",
        "Glow Plum (GLPL) Solid 15",
        "Glow Plum (GLPL) Solid 25",
        "Glow Plum (GLPL) Solid 35",
        "Glow Plum (GLPL) Solid 50",
        "Glow Plum (GLPL) Grad 15",
        "Glow Plum (GLPL) Grad 25",
        "Glow Plum (GLPL) Grad 35",
        "Glow Plum (GLPL) Grad 50",
        "Glow Plum (GLPL) Double 50 / 20"
      ],
      GLBD: [
        "Glow Bordeaux (GLBD) Solid 10",
        "Glow Bordeaux (GLBD) Solid 15",
        "Glow Bordeaux (GLBD) Solid 25",
        "Glow Bordeaux (GLBD) Solid 35",
        "Glow Bordeaux (GLBD) Solid 50",
        "Glow Bordeaux (GLBD) Grad 15",
        "Glow Bordeaux (GLBD) Grad 25",
        "Glow Bordeaux (GLBD) Grad 35",
        "Glow Bordeaux (GLBD) Grad 50",
        "Glow Bordeaux (GLBD) Double 50 / 20"
      ],
      TRPP: [
        "True Purple (TRPP) Solid 10",
        "True Purple (TRPP) Solid 15",
        "True Purple (TRPP) Solid 25",
        "True Purple (TRPP) Solid 35",
        "True Purple (TRPP) Solid 50",
        "True Purple (TRPP) Grad 15",
        "True Purple (TRPP) Grad 25",
        "True Purple (TRPP) Grad 35",
        "True Purple (TRPP) Grad 50",
        "True Purple (TRPP) Double 50 / 20"
      ],
      TRGY: [
        "True Gray (TRGY) Solid 10",
        "True Gray (TRGY) Solid 15",
        "True Gray (TRGY) Solid 25",
        "True Gray (TRGY) Solid 35",
        "True Gray (TRGY) Solid 50",
        "True Gray (TRGY) Grad 15",
        "True Gray (TRGY) Grad 25",
        "True Gray (TRGY) Grad 35",
        "True Gray (TRGY) Grad 50",
        "True Gray (TRGY) Double 50 / 20"
      ],
      TRVI: [
        "True Violet (TRVI) Solid 10",
        "True Violet (TRVI) Solid 15",
        "True Violet (TRVI) Solid 25",
        "True Violet (TRVI) Solid 35",
        "True Violet (TRVI) Solid 50",
        "True Violet (TRVI) Grad 15",
        "True Violet (TRVI) Grad 25",
        "True Violet (TRVI) Grad 35",
        "True Violet (TRVI) Grad 50",
        "True Violet (TRVI) Double 50 / 20"
      ],
      BZGN: [
        "Breeze Green (BZGN) Solid 10",
        "Breeze Green (BZGN) Solid 15",
        "Breeze Green (BZGN) Solid 25",
        "Breeze Green (BZGN) Solid 35",
        "Breeze Green (BZGN) Solid 50",
        "Breeze Green (BZGN) Grad 15",
        "Breeze Green (BZGN) Grad 25",
        "Breeze Green (BZGN) Grad 35",
        "Breeze Green (BZGN) Grad 50",
        "Breeze Green (BZGN) Double 50 / 20"
      ],
      BZNV: [
        "Breeze Navy (BZNV) Solid 10",
        "Breeze Navy (BZNV) Solid 15",
        "Breeze Navy (BZNV) Solid 25",
        "Breeze Navy (BZNV) Solid 35",
        "Breeze Navy (BZNV) Solid 50",
        "Breeze Navy (BZNV) Grad 15",
        "Breeze Navy (BZNV) Grad 25",
        "Breeze Navy (BZNV) Grad 35",
        "Breeze Navy (BZNV) Grad 50",
        "Breeze Navy (BZNV) Double 50 / 20"
      ],
      BZBL: [
        "Breeze Blue (BZBL) Solid 10",
        "Breeze Blue (BZBL) Solid 15",
        "Breeze Blue (BZBL) Solid 25",
        "Breeze Blue (BZBL) Solid 35",
        "Breeze Blue (BZBL) Solid 50",
        "Breeze Blue (BZBL) Grad 15",
        "Breeze Blue (BZBL) Grad 25",
        "Breeze Blue (BZBL) Grad 35",
        "Breeze Blue (BZBL) Grad 50",
        "Breeze Blue (BZBL) Double 50 / 20"
      ],
      COPR: [
        "Copper (COPR) Solid 50",
        "Copper (COPR) Solid 75",
        "Copper (COPR) Solid 85",
        "Copper (COPR) Grad 50",
        "Copper (COPR) Double 50 / 20"
      ],
      SMOK: [
        "Smoke (SMOK) Solid 50",
        "Smoke (SMOK) Solid 75",
        "Smoke (SMOK) Solid 85",
        "Smoke (SMOK) Grad 50",
        "Smoke (SMOK) Double 50 / 20"
      ],
      FORE: [
        "Forest (FORE) Solid 50",
        "Forest (FORE) Solid 75",
        "Forest (FORE) Solid 85",
        "Forest (FORE) Grad 50",
        "Forest (FORE) Double 50 / 20"
      ],
      SPYL: [
        "Sparky Yellow (SPYL) Solid 10",
        "Sparky Yellow (SPYL) Solid 25",
        "Sparky Yellow (SPYL) Solid 50"
      ],
      SPPK: [
        "Sparky Pink (SPPK) Solid 10",
        "Sparky Pink (SPPK) Solid 25",
        "Sparky Pink (SPPK) Solid 50"
      ],
      OLIV: [
        "Olive Twin (OLIV) Double 99 / 0"
      ],
      COTT: [
        "Cotton Twin (COTT) Double 99 / 0"
      ],
      MINT: [
        "Mint Twin (MINT) Double 99 / 0"
      ],
      ROSE: [
        "Rose Twin (ROSE) Double 99 / 0"
      ],
      Neutral: [
        "Neutral Solid 0"
      ],
      "Deep sea": [
        "Deep sea Solid 0"
      ],
      "Jade Blue": [
        "Jade Blue Solid 0"
      ],
      "Moss Green": [
        "Moss Green Solid 0"
      ],
      "Meteor Gray": [
        "Meteor Gray Solid 0"
      ],
      Creek: [
        "Creek Solid 0"
      ],
      "Iron Blue": [
        "Iron Blue Solid 0"
      ],
      "Dark Orchid": [
        "Dark Orchid Solid 0"
      ],
      "Gunmetal Gray": [
        "Gunmetal Gray Solid 0"
      ],
      "Sand Brown": [
        "Sand Brown Solid 0"
      ],
      Topazolite: [
        "Topazolite Solid 0"
      ],
      "Fire Brick": [
        "Fire Brick Solid 0"
      ],
      "River Blue": [
        "River Blue Solid 0"
      ],
      "Dark Copper": [
        "Dark Copper Solid 0"
      ],
      "FEEL BROWN": [
        "FEEL BROWN Solid 0"
      ],
      "FEEL PURPLE": [
        "FEEL PURPLE Solid 0"
      ],
      "FEEL GRAY": [
        "FEEL GRAY Solid 0"
      ],
      "FEEL PINK": [
        "FEEL PINK Solid 0"
      ],
      "OCLUA GRAY": [
        "OCLUA GRAY Solid 15",
        "OCLUA GRAY Solid 30",
        "OCLUA GRAY Solid 60"
      ],
      "OCLUA BROWN": [
        "OCLUA BROWN Solid 15",
        "OCLUA BROWN Solid 30",
        "OCLUA BROWN Solid 60"
      ],
      HDAYLIGHT: [
        "DAYLIGHT (HDAYLIGHT) Double 15 / 10",
        "DAYLIGHT (HDAYLIGHT) Double 25 / 10"
      ],
      HCACAO: [
        "CACAO (HCACAO) Double 15 / 10",
        "CACAO (HCACAO) Double 25 / 10"
      ],
      HPEONY: [
        "PEONY (HPEONY) Double 15 / 10",
        "PEONY (HPEONY) Double 25 / 10"
      ],
      HDUSK: [
        "DUSK (HDUSK) Double 15 / 10",
        "DUSK (HDUSK) Double 25 / 10"
      ],
      HVIOLET: [
        "VIOLET (HVIOLET) Double 15 / 10",
        "VIOLET (HVIOLET) Double 25 / 10"
      ],
      "Digital Filter Gray": [
        "Digital Filter Gray Solid 0"
      ],
      "Digital Filter Rose": [
        "Digital Filter Rose Solid 0"
      ],
      SAMPLE: [
        "SAMPLE Solid 0",
        "SAMPLE Grad 0",
        "SAMPLE Double 0 / 0"
      ],
      GOLF: [
        "GOLF G-OBR Solid 99",
        "GOLF G-LBR Solid 99",
        "GOLF G-DBR Solid 99",
        "GOLF G-OGN Solid 0",
        "GOLF G-DGN Solid 0",
        "GOLF BROWN1 Solid 0",
        "GOLF BROWN2 Solid 0"
      ],
      PC: [
        "PC 1 Solid 0",
        "PC 2 Solid 0"
      ],
      WALKING: [
        "WALKING 1 Solid 0",
        "WALKING 2 Solid 0"
      ],
      DRIVE: [
        "DRIVE 1 Solid 0",
        "DRIVE 2 Solid 0"
      ],
      OUTDOOR: [
        "OUTDOOR Solid 0"
      ],
      TREKKING: [
        "TREKKING Solid 0"
      ],
      FISHING: [
        "FISHING Solid 0"
      ],
      TENNIS: [
        "TENNIS Solid 0"
      ],
      ORGY: [
        "Original Gray (ORGY) Solid 50",
        "Original Gray (ORGY) Solid 75",
        "Original Gray (ORGY) Solid 85"
      ],
      HUNTING: [
        "HUNTING Solid 0"
      ],
      SHOOTING: [
        "SHOOTING Solid 0"
      ],
      MOTORCYCLING: [
        "MOTORCYCLING Solid 0"
      ],
      BOWLING: [
        "BOWLING Solid 0"
      ],
      DGGY1: [
        "DGGY1 Double 0 / 0"
      ],
      DGBR1: [
        "DGBR1 Double 0 / 0"
      ],
      DGGN1: [
        "DGGN1 Double 0 / 0"
      ],
      DGGY2: [
        "DGGY2 Double 0 / 0"
      ],
      DGBR2: [
        "DGBR2 Double 0 / 0"
      ],
      DGGN2: [
        "DGGN2 Double 0 / 0"
      ],
      ORRBG: [
        "ORRBG3 Solid 99",
        "ORRBG15 Solid 99",
        "ORRBG31 Solid 99"
      ],
      HCOR: [
        "CORAL (HCOR) Solid 10",
        "CORAL (HCOR) Solid 15",
        "CORAL (HCOR) Solid 25",
        "CORAL (HCOR) Grad 15",
        "CORAL (HCOR) Grad 25"
      ],
      HBRT: [
        "BROWN TOPAZ (HBRT) Solid 10",
        "BROWN TOPAZ (HBRT) Solid 15",
        "BROWN TOPAZ (HBRT) Solid 25",
        "BROWN TOPAZ (HBRT) Grad 15",
        "BROWN TOPAZ (HBRT) Grad 25"
      ],
      HAMP: [
        "AMETHYST PURPLE (HAMP) Solid 10",
        "AMETHYST PURPLE (HAMP) Solid 15",
        "AMETHYST PURPLE (HAMP) Solid 25",
        "AMETHYST PURPLE (HAMP) Grad 15",
        "AMETHYST PURPLE (HAMP) Grad 25"
      ],
      HKUN: [
        "KUNZITE (HKUN) Solid 10",
        "KUNZITE (HKUN) Solid 15",
        "KUNZITE (HKUN) Solid 25",
        "KUNZITE (HKUN) Grad 15",
        "KUNZITE (HKUN) Grad 25"
      ],
      HMON: [
        "MORGANITE (HMON) Solid 10",
        "MORGANITE (HMON) Solid 15",
        "MORGANITE (HMON) Solid 25",
        "MORGANITE (HMON) Grad 15",
        "MORGANITE (HMON) Grad 25"
      ],
      HIDL: [
        "INDIGOLITE (HIDL) Solid 10",
        "INDIGOLITE (HIDL) Solid 15",
        "INDIGOLITE (HIDL) Solid 25",
        "INDIGOLITE (HIDL) Grad 15",
        "INDIGOLITE (HIDL) Grad 25"
      ],
      HTAN: [
        "TANZANITE (HTAN) Solid 10",
        "TANZANITE (HTAN) Solid 15",
        "TANZANITE (HTAN) Solid 25",
        "TANZANITE (HTAN) Grad 15",
        "TANZANITE (HTAN) Grad 25"
      ],
      HBNBR: [
        "NOBLE BROWN (HBNBR) Solid 8",
        "NOBLE BROWN (HBNBR) Solid 20",
        "NOBLE BROWN (HBNBR) Solid 40",
        "NOBLE BROWN (HBNBR) Solid 80",
        "NOBLE BROWN (HBNBR) Grad 20",
        "NOBLE BROWN (HBNBR) Grad 40",
        "NOBLE BROWN (HBNBR) Grad 80"
      ],
      HBCMV: [
        "CLEAR MAUVE (HBCMV) Solid 8",
        "CLEAR MAUVE (HBCMV) Solid 20",
        "CLEAR MAUVE (HBCMV) Solid 40",
        "CLEAR MAUVE (HBCMV) Solid 80",
        "CLEAR MAUVE (HBCMV) Grad 20",
        "CLEAR MAUVE (HBCMV) Grad 40",
        "CLEAR MAUVE (HBCMV) Grad 80"
      ],
      HBSGY: [
        "SHEER GRAY (HBSGY) Solid 8",
        "SHEER GRAY (HBSGY) Solid 20",
        "SHEER GRAY (HBSGY) Solid 40",
        "SHEER GRAY (HBSGY) Solid 80",
        "SHEER GRAY (HBSGY) Grad 20",
        "SHEER GRAY (HBSGY) Grad 40",
        "SHEER GRAY (HBSGY) Grad 80"
      ],
      ACVGOLF: [
        "ACVGOLF OBR Solid 0",
        "ACVGOLF LBR Solid 0",
        "ACVGOLF DBR Solid 0"
      ],
      ACVWALK: [
        "ACVWALK Solid 0"
      ],
      ACVDRIVE: [
        "ACVDRIVE Solid 0"
      ],
      ACVPC: [
        "ACVPC Solid 0"
      ],
      SKGY: [
        "Sky Gray (SKGY) Solid 10",
        "Sky Gray (SKGY) Solid 15",
        "Sky Gray (SKGY) Solid 25",
        "Sky Gray (SKGY) Solid 35",
        "Sky Gray (SKGY) Solid 50",
        "Sky Gray (SKGY) Grad 15",
        "Sky Gray (SKGY) Grad 25",
        "Sky Gray (SKGY) Grad 35",
        "Sky Gray (SKGY) Grad 50",
        "Sky Gray (SKGY) Double 50 / 20"
      ],
      SDGY: [
        "Shadow Gray (SDGY) Solid 10",
        "Shadow Gray (SDGY) Solid 15",
        "Shadow Gray (SDGY) Solid 25",
        "Shadow Gray (SDGY) Solid 35",
        "Shadow Gray (SDGY) Solid 50",
        "Shadow Gray (SDGY) Grad 15",
        "Shadow Gray (SDGY) Grad 25",
        "Shadow Gray (SDGY) Grad 35",
        "Shadow Gray (SDGY) Grad 50",
        "Shadow Gray (SDGY) Double 50 / 20"
      ],
      GCBL: [
        "Grace Blue (GCBL) Solid 10",
        "Grace Blue (GCBL) Solid 15",
        "Grace Blue (GCBL) Solid 25",
        "Grace Blue (GCBL) Solid 35",
        "Grace Blue (GCBL) Solid 50",
        "Grace Blue (GCBL) Grad 15",
        "Grace Blue (GCBL) Grad 25",
        "Grace Blue (GCBL) Grad 35",
        "Grace Blue (GCBL) Grad 50",
        "Grace Blue (GCBL) Double 50 / 20"
      ],
      CLBL: [
        "Clear Blue (CLBL) Solid 10",
        "Clear Blue (CLBL) Solid 15",
        "Clear Blue (CLBL) Solid 25",
        "Clear Blue (CLBL) Grad 15",
        "Clear Blue (CLBL) Grad 25"
      ],
      SLGY: [
        "Slate Gray (SLGY) Solid 50",
        "Slate Gray (SLGY) Solid 75",
        "Slate Gray (SLGY) Solid 85",
        "Slate Gray (SLGY) Grad 50",
        "Slate Gray (SLGY) Double 50 / 20",
        "Slate Gray (SLGY) 75/25 Solid 0"
      ],
      BTBR: [
        "Bistre Brown (BTBR) 75/25 Solid 0"
      ],
      GGY: [
        "GGY Gray Double 85 / 30"
      ],
      GBR: [
        "GBR Brown Double 85 / 30"
      ],
      GGN: [
        "GGN Green Double 85 / 30"
      ],
      "Fine Purple": [
        "Fine Purple (F PP) Solid 10",
        "Fine Purple (F PP) Solid 15",
        "Fine Purple (F PP) Solid 20",
        "Fine Purple (F PP) Grad 10",
        "Fine Purple (F PP) Grad 15",
        "Fine Purple (F PP) Grad 20"
      ],
      "Fine Pink": [
        "Fine Pink (F OR) Solid 15",
        "Fine Pink (F OR) Solid 20",
        "Fine Pink (F OR) Grad 15",
        "Fine Pink (F OR) Grad 20"
      ],
      "Fine Green": [
        "Fine Green (F GR) Solid 15",
        "Fine Green (F GR) Solid 20",
        "Fine Green (F GR) Grad 15",
        "Fine Green (F GR) Grad 20"
      ],
      "Fine Brown": [
        "Fine Brown (F BG) Solid 15",
        "Fine Brown (F BG) Solid 20",
        "Fine Brown (F BG) Grad 15",
        "Fine Brown (F BG) Grad 20"
      ],
      "Fine Gray": [
        "Fine Gray (F GY) Solid 15",
        "Fine Gray (F GY) Solid 20",
        "Fine Gray (F GY) Grad 15",
        "Fine Gray (F GY) Grad 20"
      ],"None": [
        "None",
      ]
    };

    colorGroupSelect.addEventListener('change', function () {
      const selectedColorGroup = colorGroupSelect.value;
      const options = optionsData[selectedColorGroup] || [];

      nameTypeDensitySelect.innerHTML = '<option value="" disabled selected>Select option</option>';
      options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        nameTypeDensitySelect.appendChild(optionElement);
      });
    });