### Issue Summary
- **Duration of the Outage**: August 18, 2024, 10:00 AM - 11:30 AM (EAT)
- **Impact**: The main website of Starlink Translation Centre experienced a complete outage, causing a 100% downtime. Users were unable to access the site, leading to a loss of service for approximately 85% of active users.
- **Root Cause**: A misconfiguration in the Nginx server settings during a routine update led to a failure in the server’s ability to handle incoming traffic.

### Timeline
- **10:00 AM**: Issue detected through a monitoring alert that reported the website as unreachable.
- **10:05 AM**: The DevOps team began investigating the Nginx server, suspecting a hardware failure.
- **10:15 AM**: Assumptions led to checking the load balancer configuration, which appeared to be working fine.
- **10:25 AM**: The issue was escalated to the Web Operations team after the DevOps team was unable to find the root cause.
- **10:40 AM**: The Web Operations team discovered a recent change in the Nginx configuration that had not been thoroughly tested.
- **11:00 AM**: The misconfiguration was corrected, and the server was restarted.
- **11:30 AM**: The website was back online, and normal operations were resumed.

### Root Cause and Resolution
- **Root Cause**: The issue stemmed from a recent update to the Nginx server configuration, where an incorrect directive was introduced, preventing Nginx from processing incoming HTTP requests correctly. The error was not caught during the initial testing phase due to a lack of thorough testing in a staging environment.
- **Resolution**: The incorrect configuration was identified and corrected by the Web Operations team. The Nginx server was then restarted to apply the correct settings, restoring normal functionality.

### Corrective and Preventative Measures
- **Improvements**: Implement a more rigorous testing protocol for server configuration changes, including testing in a staging environment that mirrors production.
- **Specific Tasks**:
  - Patch Nginx server to handle improper directives more gracefully.
  - Add monitoring specifically for Nginx configuration errors.
  - Review and update the deployment process to include additional checks before applying changes to the production environment.

---

