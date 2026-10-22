fetch("./stats.json")
    .then(response => response.json())
    .then(/**
     * Fill the page's statistics elements from the parsed stats.json data.
     *
     * @param {Object} data - Combined Jellyfin, Seerr, Immich, and Tracearr statistics.
     * @throws {TypeError} If data is null or undefined, or a target element is missing.
     */ data => {
      document.getElementById("movie-count").textContent = data.MovieCount;
      document.getElementById("episode-count").textContent = data.EpisodeCount;
      document.getElementById("song-count").textContent = data.SongCount;
      document.getElementById("requests-total").textContent = data.RequestsTotal;
      document.getElementById("requests-pending").textContent = data.RequestsPending;
      document.getElementById("requests-approved").textContent = data.RequestsApproved;
      document.getElementById("immich-photos").textContent = data.Photos;
      document.getElementById("immich-videos").textContent = data.Videos;
      document.getElementById("immich-disk").textContent = data.Disk;
      document.getElementById("immich-diskav").textContent = data.DiskAv;
      document.getElementById("tracearr-streams").textContent = data.ActiveStreams;
      document.getElementById("tracearr-sessions").textContent = data.TotalSessions;
      document.getElementById("tracearr-users").textContent = data.TotalUsers;
      //document.getElementById("series-count").textContent = data.SeriesCount;
    });
  //i dont know the exact stackoverflow page i got this from but all this does is grab the stats from stats.json
  //and stores it as i call it "html variables" so that the html can display the stats