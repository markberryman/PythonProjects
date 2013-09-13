using System;
using System.Collections.Generic;
using System.Web.Http;

namespace WebFrontEnd.Controllers {
    public class StatsController : ApiController {
        public struct SystemStats {
            public DateTime StatsDate { get; set; }
            public long NumJobsProcessed { get; set; }
        }

        // GET api/stats
        public SystemStats Get() {
            var ss = new SystemStats {
                StatsDate = DateTime.Now,
                NumJobsProcessed = DateTime.Now.Ticks
            };

            return ss;
        }
    }
}
