javascript: (function () {
  const userInput = prompt(
    "表示したいバージョンを選択してください: 1 (classic), 2 (white), 3 (gold)\n複数選択する場合はカンマ区切りで入力 (例: 1,3)"
  );
  const versionSelections = userInput
    .split(",")
    .map((selection) => selection.trim());
  let versionRanges = [];
  versionSelections.forEach((selection) => {
    switch (selection) {
      case "1":
        versionRanges.push([1, 13]);
        break;
      case "2":
        versionRanges.push([14, 16]);
        break;
      case "3":
        versionRanges.push([17, 20]);
        break;
      default:
        alert(
          "無効な入力です。1, 2, 3のいずれかをカンマ区切りで入力してください。"
        );
        return;
    }
  });
  document.querySelectorAll(".div-jacket").forEach(function (div) {
    const title = div.firstChild.getAttribute("title");
    if (title) {
      const trimmedTitle = title.trim();
      const songData = ALL_SONG_DATA.find(
        (song) => song.song_name.trim() === trimmedTitle
      );
      if (songData) {
        const isInSelectedRange = versionRanges.some(
          (range) =>
            songData.version_num >= range[0] && songData.version_num <= range[1]
        );
        div.style.display = isInSelectedRange ? "" : "none";
      }
    }
  });
})();
