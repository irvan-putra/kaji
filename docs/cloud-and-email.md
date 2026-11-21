# NEO App and Excellent: public services

Checked 21 November 2026. Public-source service explanation, not a benchmark or procurement verdict.

  Kaji  / Public service notes · 21 Nov 2026 
 Run an app, or run business email? 
 Biznet GIO's NEO App and Excellent solve different starting problems.  NEO App is an application deployment platform.   Excellent offers managed email and infrastructure services, alongside licensing, support and training.  They are not direct substitutes just because both involve servers. 
 This is a public-source explainer, checked 21 November 2026. Product features and commercial terms below are the vendors' advertised descriptions, not an independent performance, security or email-deliverability test. 
 The short version 
    Need  Relevant service  What to establish first    
  Put application code online  Biznet GIO NEO App: source or image deployment, runtime, HTTPS and managed backend components.  Runtime support, persistent data, full resource cost, backups and an exit path.  
  Operate company email on a domain  Excellent Managed Services Email Server: Zimbra on VPS/cloud with server operation handled by Excellent.  Users, mailbox sizes, licensing, migration, location, recovery and support scope.  
  Maintain existing mail or virtualization infrastructure  Excellent's Zimbra support, patching and training; Proxmox implementation and licensing services.  Who owns each operational task, supported versions, response times and maintenance windows.  
  
 Biznet GIO NEO App: from code to a running service 
  NEO App's official product page  describes a platform as a service (PaaS). Instead of starting by configuring a server over SSH, developers supply application code or a container and use the platform's build and deployment flow. 
 
  Deployment inputs:  Git repositories, ZIP or tar.gz source archives, templates, Dockerfiles and prebuilt container images. The page also advertises AI-agent deployment through MCP. 
  Application types:  public web applications, static sites and background workers. Listed runtimes include Node.js, Python, Go and PHP/Laravel, with framework and monorepo detection. 
  Backend building blocks:  managed PostgreSQL, NATS queues, cron jobs and S3 object storage are advertised. Their presence does not mean every component is included in one compute price. 
  Operations:  automatic HTTPS, an app.neoapp.id subdomain, custom-domain support, logs, resource graphs, a browser terminal and rollback. The vendor advertises horizontal autoscaling; its scale-to-zero description specifically discusses idle background workers. Check eligibility rather than assuming all services stop billing when idle. 
 
  Public commercial snapshot:  the page advertises “starting from Rp50/hour,” top-ups starting at Rp100,000, no monthly contract, and free bandwidth egress, subdomain and SSL. These are public headline terms as checked on 21 November 2026, not a quote for any particular configuration or account. Confirm applicable tax, resources, databases, storage, replicas, limits and billing behavior before deployment. The headline rate is not a complete application budget. 
  What this does not establish:  the product page is not a benchmark, a recovery test or evidence that an application is secure. Runtime compatibility, app dependencies, secrets, data retention, backups, observability and deployment rollback still need a project-specific check. A rollback of code is not automatically a rollback or backup of database contents. 
 Excellent: managed email and infrastructure expertise 
  Excellent's product and services page  lists Zimbra, Proxmox, SSL certificates, support and maintenance, technical books/modules, and training. Its  Zimbra service page  covers installation, upgrades and patching, repairs, managed services, Network Edition licensing and training. 
 Managed Zimbra email 
 The  Excellent Managed Services page  describes Zimbra email hosted on VPS/cloud infrastructure prepared and managed by its team. Advertised work includes setup, updates, hardening and performance tuning. It also describes an anti-spam/anti-virus gateway option, authenticated SMTP relay, and MX backup. 
 Those features address different jobs. A mail platform runs mailboxes and collaboration; a spam gateway filters traffic; a relay handles outgoing delivery; MX backup temporarily queues incoming mail during an outage and forwards it when the primary service returns.  MX queuing is not the same as a complete mailbox backup and restore service.  Ask separately about retention, restore points, deletion recovery and tested recovery times. 
 The vendor says its authenticated relay can help sending reputation and reduce legitimate mail landing in spam. That is a service claim, not a guarantee of inbox placement. This note does not independently rate Excellent's IP reputation or mail deliverability. 
 Beyond email 
 
  Proxmox:  Excellent lists Proxmox Mail Gateway licensing and Proxmox Virtual Environment implementation. These are distinct products: a mail security gateway versus a virtualization platform.  Proxmox's own VE overview  describes management of virtual machines and containers, with compute, networking and storage. 
  SSL certificates:  its services page lists single-domain, multi-domain, wildcard and extended-validation certificates. Confirm current issuer, validation requirements and renewal ownership rather than treating older partner names as a current certification check. 
  Support and training:  mail-server maintenance and Linux, virtualization and mail-server training are listed, with regular, special, in-house and online formats. Availability and exact scope need confirmation. 
 
 Excellent's published cost notes need a full quote 
 The EMS page publishes important exclusions and conditions. As checked on 21 November 2026, it says: 
 
 Prices exclude VAT; domain and hosting charges are separate from package charges. 
 Its stated package location is Singapore, with a 20% package surcharge for Indonesia. 
 Setup is Rp1,000,000 for Bronze–Silver and Rp1,500,000 for Gold–Premium; annual upfront payment waives setup. 
 Monthly payment is upfront. Zimbra Network Edition licensing is excluded and charged per user account. 
 A standard single-domain SSL certificate is listed at Rp500,000/year. Migration is an additional service priced according to the amount of data; multi-server charges multiply by server count. 
 
 These are published notes, not a verified all-in package quotation. Base package pricing was not readable in the fetched page text, so no monthly package total is asserted here. Confirm whether the current proposal still uses these terms, which items overlap with hosting, and the exact tax-inclusive total. A managed email budget depends on users, storage, licensing, server count, location, migration and support scope, not just one headline number. 
 A fair comparison follows the workload 
 For an app, evaluate NEO App's deployment flow, data services, resource billing and portability. For managed company email, evaluate Excellent's operating scope, migration, licensing and recovery commitments. They can be complementary rather than competing services. 
 Biznet GIO also advertises a separate  VPS Zimbra product . That is a closer starting point for an email-service comparison than NEO App. It is a different product: do not transfer NEO App's features or pricing to it, and compare management responsibilities and inclusions explicitly. 
 Questions before choosing 
 
  Application hosting:  Which resources keep billing when idle? What survives redeployment? How are backups restored? What costs apply to databases, storage and autoscaling? Can code and data be exported without proprietary dependencies? 
  Business email:  Who controls the domain and DNS? Who sets and maintains SPF, DKIM and DMARC? Are relay IPs shared or dedicated? What are the sending limits, abuse rules and incident response times? 
  Managed service:  What are the uptime and support commitments, recovery point/time targets, data location, maintenance schedule, access controls and exit/migration terms? Request these in writing. 
 
 Source ledger 
 Official product and documentation pages opened on 21 November 2026. Vendor claims are attributed above; no independent ranking or procurement recommendation is implied. 
 
  Biznet GIO: NEO App  — deployment routes, components, advertised features and public headline commercial terms. 
  Excellent: Products and Services  — service categories. 
  Excellent Managed Services  — managed email scope, relay, MX backup and published cost conditions. 
  Excellent: Zimbra  — installation, patching, support, licensing and training. 
  Biznet GIO: VPS Zimbra  — separate email-hosting product, not NEO App. 
  Proxmox VE overview  — virtualization category and components. 
 
  Kaji  · Public information only. No account information, customer-specific quotes or private recommendations are included. Vendor offerings and prices can change. 

## Source URLs

- https://www.biznetgio.com/product/neo-app-platform
- https://www.excellent.co.id/product-services/
- https://www.excellent.co.id/zimbra/
- https://zimbra.excellent.co.id/ems
- https://www.proxmox.com/en/products/proxmox-virtual-environment/overview
- https://www.biznetgio.com/product/vps-zimbra
