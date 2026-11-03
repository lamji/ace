# ACE Exam Review Index

**Score: 35 / 238 (15%)**: 26 incorrect, 177 didn't know

| # | Topic | My Answer | Correct | Result | File |
|---|---|---|---|---|---|
| 1 | IAM + Compute Engine (OS Login) | C | C | ✅ | [Q001-os-login.md](Q001-os-login.md) |
| 2 | VPC networking (CIDR, private ranges) | B | B | ✅ | [Q002-vpc-subnet-cidr.md](Q002-vpc-subnet-cidr.md) |
| 3 | Databases (Cloud SQL PITR vs Spanner) | A | A | ✅ | [Q003-cloud-sql-pitr.md](Q003-cloud-sql-pitr.md) |
| 4 | Compute Engine (MIG autohealing vs autoscaling) | C | C | ✅ | [Q004-mig-autohealing.md](Q004-mig-autohealing.md) |
| 5 | gcloud CLI (named configurations vs kubectl contexts) | A | A | ✅ | [Q005-gcloud-configurations.md](Q005-gcloud-configurations.md) |
| 6 | Cloud Storage (storage classes for DR backups) | D | D | ✅ | [Q006-storage-class-disaster-recovery.md](Q006-storage-class-disaster-recovery.md) |
| 7 | Billing (create billing account, link projects) | D | D | ✅ | [Q007-centralize-billing-account.md](Q007-centralize-billing-account.md) |
| 8 | VPC networking (static internal IP vs ephemeral/public) | A | A | ✅ | [Q008-static-internal-ip.md](Q008-static-internal-ip.md) |
| 9 | App Engine (automatic vs basic vs manual scaling) | D | D | ✅ | [Q009-app-engine-scaling.md](Q009-app-engine-scaling.md) |
| 10 | IAM (copy custom roles to another project) | A | A | ✅ | [Q010-copy-iam-custom-roles.md](Q010-copy-iam-custom-roles.md) |
| 11 | Infrastructure as Code (Deployment Manager vs Composer vs instance groups) | A | A | ✅ | [Q011-deployment-manager-iac.md](Q011-deployment-manager-iac.md) |
| 12 | GKE (Dockerfile → image → registry → kubectl) | C | C | ✅ | [Q012-deploy-dockerfile-gke.md](Q012-deploy-dockerfile-gke.md) |
| 13 | Cloud Marketplace (Jenkins click-to-deploy) | D | D | ✅ | [Q013-jenkins-marketplace.md](Q013-jenkins-marketplace.md) |
| 14 | Deployment Manager (deployments update vs create vs resources) | B | B | ✅ | [Q014-deployment-manager-update.md](Q014-deployment-manager-update.md) |
| 15 | BigQuery (dry run, bytes read vs returned, on-demand cost) | B | B | ✅ | [Q015-bigquery-dry-run-cost.md](Q015-bigquery-dry-run-cost.md) |
| 16 | Compute Engine (MIG CPU autoscaling vs schedule vs GKE HPA) | B | B | ✅ | [Q016-mig-cpu-autoscaling.md](Q016-mig-cpu-autoscaling.md) |
| 17 | Billing (export to BigQuery + SQL cost analysis) | D | D | ✅ | [Q017-billing-export-bigquery.md](Q017-billing-export-bigquery.md) |
| 18 | Cloud Storage (lifecycle rules, Age from creation) | B | B | ✅ | [Q018-storage-lifecycle-age.md](Q018-storage-lifecycle-age.md) |
| 19 | IAM + Compute Engine (attach service account to VM, avoid JSON keys) | — | A | ❓ Didn't know | [Q019-vm-service-account.md](Q019-vm-service-account.md) |
| 20 | Compute Engine (Windows VM: RDP, Windows password, port 3389) | A | D | ❌ | [Q020-rdp-windows-vm.md](Q020-rdp-windows-vm.md) |
| 21 | Cloud SDK / gcloud CLI (two configurations: create, then activate to switch) | — | A | ❓ Didn't know | [Q021-gcloud-multiple-configurations.md](Q021-gcloud-multiple-configurations.md) |
| 22 | Deployment Manager (--preview before committing) | D | D | ✅ | [Q022-deployment-manager-preview.md](Q022-deployment-manager-preview.md) |
| 23 | Data pipeline (Pub/Sub → Dataflow → Bigtable + BigQuery, time-series) | C | D | ❌ | [Q023-time-series-pipeline.md](Q023-time-series-pipeline.md) |
| 24 | App Engine (new prod project: create project, then deploy) | C | A | ❌ | [Q024-app-engine-new-prod-project.md](Q024-app-engine-new-prod-project.md) |
| 25 | IAM (auditors: group + predefined roles logging.viewer, bigquery.dataViewer) | C | A | ❌ | [Q025-bigquery-auditors-group-roles.md](Q025-bigquery-auditors-group-roles.md) |
| 26 | IAM + Cloud Storage (service account + storage.objectCreator on one bucket) | C | C | ✅ | [Q026-vm-write-bucket-objectcreator.md](Q026-vm-write-bucket-objectcreator.md) |
| 27 | Cloud Logging (Data Access audit logs in Logs Explorer vs Activity page) | A | B | ❌ | [Q027-storage-data-access-logs.md](Q027-storage-data-access-logs.md) |
| 28 | IAM + Cloud Storage (Storage Admin vs Object Admin vs Editor) | B | B | ✅ | [Q028-storage-admin-buckets-and-files.md](Q028-storage-admin-buckets-and-files.md) |
| 29 | Cloud Storage (signed URL vs public object / lifecycle) | B | A | ❌ | [Q029-signed-url-external-share.md](Q029-signed-url-external-share.md) |
| 30 | GKE workloads (DaemonSet = one pod per node, vs StatefulSet / Deployment) | — | B | ❓ Didn't know | [Q030-gke-daemonset-monitoring.md](Q030-gke-daemonset-monitoring.md) |
| 31 | APIs & Services (enable Pub/Sub API in API Library; no auto-enable) | A | A | ✅ | [Q031-enable-pubsub-api.md](Q031-enable-pubsub-api.md) |
| 32 | Cloud Monitoring (one Stackdriver account / metrics scope, link all projects) | D | C | ❌ | [Q032-monitoring-multiple-projects.md](Q032-monitoring-multiple-projects.md) |
| 33 | Compute Engine MIG (autoscaling On, min 1 / max 1 = exactly one VM) | B | A | ❌ | [Q033-mig-single-instance-always-on.md](Q033-mig-single-instance-always-on.md) |
| 34 | IAM (IAM page = who has which role; Roles page = role catalog) | D | C | ❌ | [Q034-verify-iam-members-roles.md](Q034-verify-iam-members-roles.md) |
| 35 | Billing (create NEW billing account, link EXISTING project; Project Billing Manager) | B | B | ✅ | [Q035-new-billing-account-link-project.md](Q035-new-billing-account-link-project.md) |
| 36 | IAM cross-project (grant SA Compute Storage Admin in proj-vm; scopes/keys are wrong) | D | C | ❌ | [Q036-cross-project-sa-snapshots.md](Q036-cross-project-sa-snapshots.md) |
| 37 | App Engine (region is permanent, one app per project → new project) | B | D | ❌ | [Q037-app-engine-change-region.md](Q037-app-engine-change-region.md) |
| 38 | IAM + Cloud Spanner (databaseUser role, group access) | B | B | ✅ | [Q038-spanner-databaseuser-group.md](Q038-spanner-databaseuser-group.md) |
| 39 | GKE (node auto-upgrades vs auto-repair, version vs node image) | D | B | ❌ | [Q039-gke-node-auto-upgrades.md](Q039-gke-node-auto-upgrades.md) |
| 40 | Cloud Load Balancing (public HTTPS, TLS termination, HTTP(S) vs TCP) | A | A | ✅ | [Q040-https-load-balancer-tls-termination.md](Q040-https-load-balancer-tls-termination.md) |
| 41 | Cloud Storage (parallel composite uploads, throughput, Nearline caveat) | — | B | ❓ | [Q041-large-file-parallel-upload.md](Q041-large-file-parallel-upload.md) |
| 42 | Kubernetes / GKE (database password in Secret vs ConfigMap, image, volume) | B | B | ✅ | [Q042-kubernetes-secret-database-password.md](Q042-kubernetes-secret-database-password.md) |
| 43 | Compute Engine MIG (autoscaling, health-check startup delay) | C | D | ❌ | [Q043-mig-autoscaling-startup-delay.md](Q043-mig-autoscaling-startup-delay.md) |
| 44 | Compute Engine (nightly batch jobs, Spot/preemptible VMs vs GKE/micro bursting) | A | C | ❌ | [Q044-batch-jobs-spot-vms.md](Q044-batch-jobs-spot-vms.md) |
| 46 | App Engine + gcloud CLI (active project configuration vs app.yaml) | A | D | ❌ | [Q046-app-engine-gcloud-project-config.md](Q046-app-engine-gcloud-project-config.md) |
| 47 | Compute Engine (instance template, automatic restart, host maintenance migration vs autohealing) | C | A | ❌ | [Q047-compute-engine-maintenance-restart.md](Q047-compute-engine-maintenance-restart.md) |
| 48 | Cloud Storage (PDF object Content-Type vs public access, CDN, bucket labels) | B | C | ❌ | [Q048-cloud-storage-pdf-content-type.md](Q048-cloud-storage-pdf-content-type.md) |
| 49 | Compute Engine (stop → increase memory / custom machine type → start) | D | D | ✅ | [Q049-vm-increase-memory.md](Q049-vm-increase-memory.md) |
| 50 | VPC networking (one VPC, 2 subnets, non-overlapping CIDR; VPC global) | B | A | ❌ | [Q050-vpc-two-subnets-prod-test.md](Q050-vpc-two-subnets-prod-test.md) |
| 52 | IAM + BigQuery (group + jobUser to run queries; dataViewer can't query) | D | C | ❌ | [Q052-bigquery-jobuser-group.md](Q052-bigquery-jobuser-group.md) |
| 53 | VPC firewall (ingress, target/source by service account, TCP:8080 only) | B | B | ✅ | [Q053-firewall-tiers-service-accounts.md](Q053-firewall-tiers-service-accounts.md) |
| 54 | VPC networking (new region → new subnet in the same global VPC) | A | A | ✅ | [Q054-new-region-subnet-same-vpc.md](Q054-new-region-subnet-same-vpc.md) |
| 55 | Cloud Logging (exclude noisy GKE container logs at ingestion) | A | A | ✅ | [Q055-disable-gke-container-logs.md](Q055-disable-gke-container-logs.md) |
| 56 | App Engine (traffic splitting --splits 99/1 vs --migrate; one app per project) | B | B | ✅ | [Q056-app-engine-traffic-split.md](Q056-app-engine-traffic-split.md) |
| 57 | Compute Engine MIG (rolling update: maxSurge 1, maxUnavailable 0 keeps capacity) | — | B | ❓ Didn't know | [Q057-mig-rolling-update-maxsurge.md](Q057-mig-rolling-update-maxsurge.md) |
| 58 | Databases (relational + global + unknown scale → Spanner; Firestore/Datastore are NoSQL) | D | B | ❌ | [Q058-global-relational-db-spanner.md](Q058-global-relational-db-spanner.md) |
| 59 | IAM + Billing (finance: Billing Account User on account + Project Billing Manager on org) | C | C | ✅ | [Q059-finance-link-billing-roles.md](Q059-finance-link-billing-roles.md) |
| 60 | GKE + Networking (internal LB annotation + VPC peering; Cloud Armor doesn't connect VPCs) | D | C | ❌ | [Q060-gke-internal-lb-vpc-peering.md](Q060-gke-internal-lb-vpc-peering.md) |
| 61 | Cloud Logging + Storage (audit logs 3 years → sink to Coldline bucket; BigQuery = analysis) | — | B | ❓ Didn't know | [Q061-audit-logs-sink-coldline.md](Q061-audit-logs-sink-coldline.md) |
| 62 | Memorystore vs custom machine type (32 GB RAM, almost no CPU; debated A vs B) | — | A | ❓ Didn't know | [Q062-reverse-proxy-memory-custom-vm.md](Q062-reverse-proxy-memory-custom-vm.md) |
| 63 | Hybrid networking (on-prem no internet → VPN + Cloud Router 199.36.153.4/30 + DNS CNAME restricted.googleapis.com) | B | D | ❌ | [Q063-onprem-private-google-access.md](Q063-onprem-private-google-access.md) |
| 64 | Cloud Run + Pub/Sub (push subscription + service account with Cloud Run Invoker) | C | C | ✅ | [Q064-pubsub-push-cloud-run.md](Q064-pubsub-push-cloud-run.md) |
| 65 | Compute choice (container + HTTP + few requests → Cloud Run scales to zero; container ≠ GKE) | D | A | ❌ | [Q065-low-traffic-container-cloud-run.md](Q065-low-traffic-container-cloud-run.md) |
| 66 | Billing (one invoice by tomorrow → link acquired projects to your billing account; no migration) | D | A | ❌ | [Q066-acquisition-single-invoice-link-billing.md](Q066-acquisition-single-invoice-link-billing.md) |
| 67 | IAM (monitor Spanner, no table data → monitoring.viewer; databaseReader reads rows) | C | A | ❌ | [Q067-spanner-support-monitoring-viewer.md](Q067-spanner-support-monitoring-viewer.md) |
| 68 | Cloud Logging (filtered sink → BigQuery dataset; no Pub/Sub + Functions) | C | C | ✅ | [Q068-compute-logs-sink-bigquery.md](Q068-compute-logs-sink-bigquery.md) |
| 69 | Deployment Manager (Type Provider for cluster API → DaemonSet in same deployment) | A | A | ✅ | [Q069-deployment-manager-type-provider-daemonset.md](Q069-deployment-manager-type-provider-daemonset.md) |
| 70 | IAM (on-prem app → create service account key file; Interconnect ≠ auth; never a user account) | A | B | ❌ | [Q070-onprem-service-account-key-file.md](Q070-onprem-service-account-key-file.md) |
| 71 | IAM + GKE (pull images from Container Registry in another project → Storage Object Viewer for node SA) | — | A | ❓ Didn't know | [Q071-gke-pull-images-other-project.md](Q071-gke-pull-images-other-project.md) |
| 72 | GKE troubleshooting (Pending pod → describe the pod, read events; no logs yet) | — | C | ❓ Didn't know | [Q072-gke-pod-pending-describe.md](Q072-gke-pod-pending-describe.md) |
| 73 | Compute Engine (Windows VM RDP → gcloud compute reset-windows-password) | — | B | ❓ Didn't know | [Q073-windows-vm-rdp-password.md](Q073-windows-vm-rdp-password.md) |
| 74 | IAM + Compute Engine (SSH one VM for a group → OS Login + compute.osLogin) | — | A | ❓ Didn't know | [Q074-ssh-one-instance-oslogin.md](Q074-ssh-one-instance-oslogin.md) |
| 75 | gcloud (enabled APIs → projects list for ID, services list --project; --available = all) | — | A | ❓ Didn't know | [Q075-list-enabled-apis-gcloud.md](Q075-list-enabled-apis-gcloud.md) |
| 76 | App Engine (1% test → new version + split traffic; one app per project) | — | D | ❓ Didn't know | [Q076-app-engine-split-traffic-console.md](Q076-app-engine-split-traffic-console.md) |
| 77 | Pricing calculator (high IOPS → local SSD; snapshots → persistent disk + snapshot storage) | — | A | ❓ Didn't know | [Q077-gke-pricing-calculator-local-ssd.md](Q077-gke-pricing-calculator-local-ssd.md) |
| 78 | GKE networking (public HTTPS → NodePort Service + Ingress; ClusterIP internal) | — | A | ❓ Didn't know | [Q078-gke-https-ingress-nodeport.md](Q078-gke-https-ingress-nodeport.md) |
| 79 | VPC networking (VMs in two projects → Shared VPC, needs an Organization) | — | B | ❓ Didn't know | [Q079-shared-vpc-two-projects.md](Q079-shared-vpc-two-projects.md) |
| 80 | IAM (auditor read all, change nothing → built-in project Viewer) | — | C | ❓ Didn't know | [Q080-auditor-project-viewer.md](Q080-auditor-project-viewer.md) |
| 81 | GKE (GPUs for one team → new GPU node pool + nodeSelector) | — | D | ❓ Didn't know | [Q081-gke-gpu-node-pool.md](Q081-gke-gpu-node-pool.md) |
| 82 | VPC networking (subnet full → gcloud expand-ip-range) | — | A | ❓ Didn't know | [Q082-expand-subnet-ip-range.md](Q082-expand-subnet-ip-range.md) |
| 83 | IAM (G Suite/Workspace users → grant IAM roles to their email) | — | B | ❓ Didn't know | [Q083-gsuite-users-iam-roles.md](Q083-gsuite-users-iam-roles.md) |
| 84 | gcloud CLI (two projects daily → gcloud configurations + script) | — | A | ❓ Didn't know | [Q084-gcloud-configurations-list-instances.md](Q084-gcloud-configurations-list-instances.md) |
| 85 | BigQuery (SQL on AVRO in Cloud Storage → external table) | — | C | ❓ Didn't know | [Q085-avro-bigquery-external-table.md](Q085-avro-bigquery-external-table.md) |
| 86 | Logging (service account created → Activity log, Configuration, Service Account) | — | A | ❓ Didn't know | [Q086-service-account-created-activity-log.md](Q086-service-account-created-activity-log.md) |
| 87 | VPC firewall (clients reach VM on UDP 636 → tag + ingress rule) | — | C | ❓ Didn't know | [Q087-firewall-ingress-udp-636-tag.md](Q087-firewall-ingress-udp-636-tag.md) |
| 88 | Billing (budget alert for one project → billing admin + project scope) | — | A | ❓ Didn't know | [Q088-budget-alert-one-project.md](Q088-budget-alert-one-project.md) |
| 89 | Compute Engine (needs 96 vCPUs → n1-standard-96 at creation) | — | A | ❓ Didn't know | [Q089-96-vcpu-n1-standard-96.md](Q089-96-vcpu-n1-standard-96.md) |
| 90 | Cloud Storage (old versions read monthly → lifecycle to Nearline) | — | B | ❓ Didn't know | [Q090-lifecycle-noncurrent-versions-nearline.md](Q090-lifecycle-noncurrent-versions-nearline.md) |
| 91 | Hybrid networking (on-prem ↔ Google Cloud private IP → Cloud VPN) | — | D | ❓ Didn't know | [Q091-burst-onprem-cloud-vpn.md](Q091-burst-onprem-cloud-vpn.md) |
| 92 | Cloud Storage (one location + yearly access → Regional + Coldline) | — | D | ❓ Didn't know | [Q092-regional-storage-coldline-compliance.md](Q092-regional-storage-coldline-compliance.md) |
| 93 | Data governance (find a column across 1000+ datasets → Data Catalog search) | — | A | ❓ Didn't know | [Q093-data-catalog-find-column.md](Q093-data-catalog-find-column.md) |
| 94 | GKE (preemptible node pool, 1 of 2 replicas Pending → node preempted, rescheduling) | — | D | ❓ Didn't know | [Q094-pending-pod-preempted-node.md](Q094-pending-pod-preempted-node.md) |
| 95 | Logging (when users added to Spanner IAM roles → Admin Activity logs) | — | D | ❓ Didn't know | [Q095-spanner-iam-admin-activity-logs.md](Q095-spanner-iam-admin-activity-logs.md) |
| 96 | BigQuery cost control (custom query quota + flat-rate slots) | — | B, E | ❓ Didn't know | [Q096-bigquery-control-query-costs.md](Q096-bigquery-control-query-costs.md) |
| 97 | GKE security (isolate arbitrary-code pods → GKE Sandbox gVisor) | — | C | ❓ Didn't know | [Q097-gke-sandbox-gvisor-isolation.md](Q097-gke-sandbox-gvisor-isolation.md) |
| 98 | Cloud Spanner (read latency → non-increasing primary key) | — | C | ❓ Didn't know | [Q098-spanner-monotonic-primary-key.md](Q098-spanner-monotonic-primary-key.md) |
| 99 | Billing (finance views reports only → billing viewer) | — | C | ❓ Didn't know | [Q099-finance-billing-viewer.md](Q099-finance-billing-viewer.md) |
| 100 | IAM (SREs approve Google Support access → group + accessapproval.approver) | — | D | ❓ Didn't know | [Q100-sre-access-approval-group.md](Q100-sre-access-approval-group.md) |
| 101 | Compute Engine (Deletion Protection) | — | D | ❓ Didn't know | [Q101-deletion-protection-shared-project.md](Q101-deletion-protection-shared-project.md) |
| 102 | IAM / BigQuery (Custom Role + Group) | — | D | ❓ Didn't know | [Q102-bigquery-custom-role-no-delete-group.md](Q102-bigquery-custom-role-no-delete-group.md) |
| 103 | Cloud SDK (Install the Emulator With apt-get) | — | C | ❓ Didn't know | [Q103-datastore-emulator-apt-install.md](Q103-datastore-emulator-apt-install.md) |
| 104 | IAM / Resource Manager (Group + Browser Role) | — | C | ❓ Didn't know | [Q104-view-hierarchy-browser-role-group.md](Q104-view-hierarchy-browser-role-group.md) |
| 105 | Identity (Third-Party IdP, Google as Service Provider) | — | B | ❓ Didn't know | [Q105-cloud-identity-saml-sso-third-party.md](Q105-cloud-identity-saml-sso-third-party.md) |
| 106 | IAM (Service Account Admin) | — | D | ❓ Didn't know | [Q106-service-account-admin-role.md](Q106-service-account-admin-role.md) |
| 107 | Cloud Storage (Coldline Storage) | — | A | ❓ Didn't know | [Q107-archive-quarterly-coldline.md](Q107-archive-quarterly-coldline.md) |
| 108 | GKE (Node Auto-Provisioning) | — | A | ❓ Didn't know | [Q108-gke-gpu-node-auto-provisioning.md](Q108-gke-gpu-node-auto-provisioning.md) |
| 109 | Identity (Google Cloud Directory Sync) | — | A | ❓ Didn't know | [Q109-ad-sync-gcds-cloud-identity.md](Q109-ad-sync-gcds-cloud-identity.md) |
| 110 | Resource hierarchy / networking (Separate Project) | — | A | ❓ Didn't know | [Q110-prod-env-new-project.md](Q110-prod-env-new-project.md) |
| 111 | IAM / Organization Policy (Temporary Cloud Identity Account + Viewer) | — | C | ❓ Didn't know | [Q111-auditor-domain-restricted-sharing.md](Q111-auditor-domain-restricted-sharing.md) |
| 112 | Compute Engine (Snapshot Schedule) | — | B | ❓ Didn't know | [Q112-boot-disk-snapshot-schedule.md](Q112-boot-disk-snapshot-schedule.md) |
| 113 | Logging / IAM (Private Logs Viewer) | — | B | ❓ Didn't know | [Q113-auditor-private-log-viewer.md](Q113-auditor-private-log-viewer.md) |
| 114 | Logging (Sink to BigQuery + Table Expiration) | — | B | ❓ Didn't know | [Q114-logs-60-days-sink-bigquery.md](Q114-logs-60-days-sink-bigquery.md) |
| 115 | Resource Manager (Project Owner + Shut Down) | — | A | ❓ Didn't know | [Q115-shut-down-project-owner.md](Q115-shut-down-project-owner.md) |
| 116 | IAM (Grant the Service Account Roles in the Data Project) | — | A | ❓ Didn't know | [Q116-cross-project-bigquery-service-account.md](Q116-cross-project-bigquery-service-account.md) |
| 117 | Logging (Data Access Audit Logs by User Email) | — | C | ❓ Didn't know | [Q117-terminated-employee-data-access-logs.md](Q117-terminated-employee-data-access-logs.md) |
| 118 | IAM (Supported Permissions + ALPHA Stage) | — | A | ❓ Didn't know | [Q118-custom-role-supported-alpha.md](Q118-custom-role-supported-alpha.md) |
| 119 | Data (Upload to Cloud Storage With gsutil) | — | B | ❓ Didn't know | [Q119-unstructured-data-dataflow-cloud-storage.md](Q119-unstructured-data-dataflow-cloud-storage.md) |
| 120 | gcloud CLI (One Configuration per Project + Activate) | — | A | ❓ Didn't know | [Q120-gcloud-configurations-multiple-projects.md](Q120-gcloud-configurations-multiple-projects.md) |
| 121 | Compute Engine (Valid Template, Leftover Disks, autoDelete) | — | C | ❓ Didn't know | [Q121-mig-instance-creation-failed-disk-autodelete.md](Q121-mig-instance-creation-failed-disk-autodelete.md) |
| 122 | Cloud Marketplace (Cloud Marketplace) | — | B | ❓ Didn't know | [Q122-cassandra-dev-marketplace.md](Q122-cassandra-dev-marketplace.md) |
| 123 | Cloud Monitoring (Cloud Monitoring Alerting Policy) | — | B | ❓ Didn't know | [Q123-cpu-alert-monitoring-policy-email.md](Q123-cpu-alert-monitoring-policy-email.md) |
| 124 | Cloud Spanner / Monitoring (Alert → Webhook → Cloud Function) | — | D | ❓ Didn't know | [Q124-spanner-autoscale-alert-webhook-function.md](Q124-spanner-autoscale-alert-webhook-function.md) |
| 125 | Billing (Billing Export to BigQuery + Scheduled Function) | — | C | ❓ Didn't know | [Q125-egress-cost-alert-billing-export-bigquery.md](Q125-egress-cost-alert-billing-export-bigquery.md) |
| 126 | Billing (Pricing Pages + Pricing Calculator) | — | A | ❓ Didn't know | [Q126-estimate-costs-pricing-calculator.md](Q126-estimate-costs-pricing-calculator.md) |
| 127 | Load balancing (SSL Proxy Load Balancer) | — | C | ❓ Didn't know | [Q127-global-ssl-tcp-ssl-proxy-lb.md](Q127-global-ssl-tcp-ssl-proxy-lb.md) |
| 128 | Compute Engine storage (Local SSD) | — | C | ❓ Didn't know | [Q128-pd-read-throttling-local-ssd.md](Q128-pd-read-throttling-local-ssd.md) |
| 129 | VPC networking (Expand the Subnet Range) | — | A | ❓ Didn't know | [Q129-expand-subnet-dataproc.md](Q129-expand-subnet-dataproc.md) |
| 130 | IAM (Other Team Grants Data Viewer to Your Service Account) | — | B | ❓ Didn't know | [Q130-app-engine-sa-bigquery-other-project.md](Q130-app-engine-sa-bigquery-other-project.md) |
| 131 | Compute Engine (Custom Image From a Snapshot, Instances From the Image) | — | D | ❓ Didn't know | [Q131-copy-vm-custom-image-from-snapshot.md](Q131-copy-vm-custom-image-from-snapshot.md) |
| 132 | Logging (Install the Logging Agent, View in Cloud Logging) | — | D | ❓ Didn't know | [Q132-vm-app-logs-install-logging-agent.md](Q132-vm-app-logs-install-logging-agent.md) |
| 133 | IAM / Cloud Storage (Storage Object Creator for the VM's Service Account) | — | B | ❓ Didn't know | [Q133-vm-sa-object-creator-other-project-bucket.md](Q133-vm-sa-object-creator-other-project-bucket.md) |
| 134 | IAM / authentication (Give the VM's Service Account Access) | — | A | ❓ Didn't know | [Q134-adc-on-vm-attached-service-account.md](Q134-adc-on-vm-attached-service-account.md) |
| 135 | Resource Manager / Compute Engine (Create Project → Enable API → Create Instance) | — | A | ❓ Didn't know | [Q135-new-project-enable-api-create-instance.md](Q135-new-project-enable-api-create-instance.md) |
| 136 | Compute Engine (Regular VM, Start and Stop as Needed) | — | C | ❓ Didn't know | [Q136-30-hour-batch-regular-vm-start-stop.md](Q136-30-hour-batch-regular-vm-start-stop.md) |
| 137 | Cloud Marketplace, CI/CD (Cloud Marketplace) | — | A | ❓ Didn't know | [Q137-jenkins-marketplace.md](Q137-jenkins-marketplace.md) |
| 138 | gcloud CLI (gcloud config set compute/zone) | — | A | ❓ Didn't know | [Q138-gcloud-config-default-zone.md](Q138-gcloud-config-default-zone.md) |
| 139 | Databases (Cloud Bigtable) | — | D | ❓ Didn't know | [Q139-sensor-events-bigtable.md](Q139-sensor-events-bigtable.md) |
| 140 | Cloud Monitoring (Workspace / Metrics Scope With All Three) | — | D | ❓ Didn't know | [Q140-monitoring-workspace-multiple-projects.md](Q140-monitoring-workspace-multiple-projects.md) |
| 141 | Billing (Billing Export to BigQuery + Data Studio) | — | A | ❓ Didn't know | [Q141-costs-multiple-billing-accounts-bigquery-datastudio.md](Q141-costs-multiple-billing-accounts-bigquery-datastudio.md) |
| 142 | VPC networking (Create It Without a Public IP) | — | A | ❓ Didn't know | [Q142-no-public-ip-instance.md](Q142-no-public-ip-instance.md) |
| 143 | Infrastructure as Code (Deployment Manager Templates in Cloud Source Repositories) | — | B | ❓ Didn't know | [Q143-iac-templates-cloud-source-repositories.md](Q143-iac-templates-cloud-source-repositories.md) |
| 144 | Compute Engine (Snapshot Schedule on the Disk) | — | B | ❓ Didn't know | [Q144-daily-snapshot-schedule-30-days-console.md](Q144-daily-snapshot-schedule-30-days-console.md) |
| 145 | GKE (Add a Node Pool With n2-highmem-16) | — | B | ❓ Didn't know | [Q145-gke-new-node-pool-highmem.md](Q145-gke-new-node-pool-highmem.md) |
| 146 | BigQuery (BigQuery External Tables) | — | D | ❓ Didn't know | [Q146-join-spanner-export-bigtable-bigquery.md](Q146-join-spanner-export-bigtable-bigquery.md) |
| 147 | High availability (VMs in Two Zones Behind a Load Balancer) | — | A | ❓ Didn't know | [Q147-survive-zone-failure-two-zones-lb.md](Q147-survive-zone-failure-two-zones-lb.md) |
| 148 | IAM (gcloud projects get-iam-policy) | — | D | ❓ Didn't know | [Q148-who-has-owner-get-iam-policy.md](Q148-who-has-owner-get-iam-policy.md) |
| 149 | VPC / GKE networking (Expand the Subnet's CIDR Range) | — | D | ❓ Didn't know | [Q149-gke-nodes-ip-exhausted-expand-subnet.md](Q149-gke-nodes-ip-exhausted-expand-subnet.md) |
| 150 | Compute Engine (Test, Then Use Preemptible VMs) | — | A | ❓ Didn't know | [Q150-fault-tolerant-batch-preemptible.md](Q150-fault-tolerant-batch-preemptible.md) |
| 151 | VPC firewall (Low-Priority Deny-All + High-Priority Allow) | — | A | ❓ Didn't know | [Q151-egress-deny-low-allow-high-priority.md](Q151-egress-deny-low-allow-high-priority.md) |
| 152 | Compute Engine access (Their Public SSH Keys on the VMs) | — | D | ❓ Didn't know | [Q152-ops-partner-no-google-accounts-ssh-keys.md](Q152-ops-partner-no-google-accounts-ssh-keys.md) |
| 153 | Serverless (Cloud Functions With a Storage Trigger) | — | B | ❓ Didn't know | [Q153-gcs-upload-trigger-cloud-functions.md](Q153-gcs-upload-trigger-cloud-functions.md) |
| 154 | Cloud Storage (Standard → Archive) | — | B | ❓ Didn't know | [Q154-lifecycle-standard-30-then-archive.md](Q154-lifecycle-standard-30-then-archive.md) |
| 155 | Logging (Enable Data Access Audit Logs for Cloud Storage) | — | D | ❓ Didn't know | [Q155-record-reads-data-access-logs-gcs.md](Q155-record-reads-data-access-logs-gcs.md) |
| 156 | Billing (One Budget per Project) | — | C | ❓ Didn't know | [Q156-budget-per-sandbox-project.md](Q156-budget-per-sandbox-project.md) |
| 157 | Compute Engine (Delete Protection) | — | B | ❓ Didn't know | [Q157-deletion-protection-production.md](Q157-deletion-protection-production.md) |
| 158 | IAM (Custom Role on the Production Project) | — | C | ❓ Didn't know | [Q158-devops-custom-role-production-project.md](Q158-devops-custom-role-production-project.md) |
| 159 | Cloud Storage (Signed URLs + Lifecycle Rule) | — | A, B | ❓ Didn't know | [Q159-signed-urls-lifecycle-45-days.md](Q159-signed-urls-lifecycle-45-days.md) |
| 160 | Infrastructure as Code (Deployment Manager Templates) | — | A | ❓ Didn't know | [Q160-iac-deployment-manager-templates.md](Q160-iac-deployment-manager-templates.md) |
| 161 | IAM (Review IAM Permissions) | — | B | ❓ Didn't know | [Q161-who-can-view-data-review-iam.md](Q161-who-can-view-data-review-iam.md) |
| 162 | Networking (Cloud DNS Private Zone + DNS Name) | — | B | ❓ Didn't know | [Q162-onprem-db-cloud-dns-private-zone.md](Q162-onprem-db-cloud-dns-private-zone.md) |
| 163 | Serverless (Cloud Run, Min Instances 0) | — | B | ❓ Didn't know | [Q163-cloud-run-min-instances-zero.md](Q163-cloud-run-min-instances-zero.md) |
| 164 | Billing (Change the Projects' Billing Account) | — | D | ❓ Didn't know | [Q164-move-projects-company-billing-account.md](Q164-move-projects-company-billing-account.md) |
| 165 | IAM (Their Service Account, Granted on Your Dataset) | — | D | ❓ Didn't know | [Q165-partner-sa-access-your-bigquery-dataset.md](Q165-partner-sa-access-your-bigquery-dataset.md) |
| 166 | Cloud Run (New Revision + Split Traffic) | — | B | ❓ Didn't know | [Q166-cloud-run-anthos-canary-revision-split.md](Q166-cloud-run-anthos-canary-revision-split.md) |
| 167 | Load balancing (External Network Load Balancer) | — | D | ❓ Didn't know | [Q167-udp-game-external-network-lb.md](Q167-udp-game-external-network-lb.md) |
| 168 | Data transfer (gsutil rsync Script on a Cron Schedule) | — | C | ❓ Didn't know | [Q168-onprem-images-gsutil-rsync-cron.md](Q168-onprem-images-gsutil-rsync-cron.md) |
| 169 | Logging (Turn On Data Access Logs, Filter in Logs Viewer) | — | A | ❓ Didn't know | [Q169-auditor-gcs-data-access-logs-query.md](Q169-auditor-gcs-data-access-logs-query.md) |
| 170 | gcloud CLI (gcloud auth activate-service-account) | — | B | ❓ Didn't know | [Q170-gcloud-activate-service-account-key.md](Q170-gcloud-activate-service-account-key.md) |
| 171 | Cloud SQL (Export to an Archive Bucket) | — | A | ❓ Didn't know | [Q171-cloud-sql-month-end-export-archive.md](Q171-cloud-sql-month-end-export-archive.md) |
| 172 | Monitoring (Log-Based Metric + Alerting Policy) | — | C | ❓ Didn't know | [Q172-notify-on-error-log-based-metric-alert.md](Q172-notify-on-error-log-based-metric-alert.md) |
| 173 | Databases (Cloud Spanner) | — | C | ❓ Didn't know | [Q173-global-relational-consistent-spanner.md](Q173-global-relational-consistent-spanner.md) |
| 174 | Compute Engine (M1 Memory-Optimized Machine Type) | — | D | ❓ Didn't know | [Q174-in-memory-erp-m1-machine-type.md](Q174-in-memory-erp-m1-machine-type.md) |
| 175 | GKE (One Deployment per Microservice) | — | D | ❓ Didn't know | [Q175-gke-deployment-per-microservice.md](Q175-gke-deployment-per-microservice.md) |
| 176 | Compute Engine (Specify It When Creating the Instance) | — | A | ❓ Didn't know | [Q176-specify-service-account-at-creation.md](Q176-specify-service-account-at-creation.md) |
| 177 | Marketplace (MongoDB Atlas From Marketplace) | — | B | ❓ Didn't know | [Q177-managed-mongodb-atlas-marketplace.md](Q177-managed-mongodb-atlas-marketplace.md) |
| 178 | IAM (BigQuery User Role to a Google Group) | — | D | ❓ Didn't know | [Q178-bi-team-bigquery-user-group.md](Q178-bi-team-bigquery-user-group.md) |
| 179 | Networking (One VPC, Two Subnets, Firewall Rules, Public Ingress to the DMZ) | — | A | ❓ Didn't know | [Q179-dmz-lan-single-vpc-two-subnets.md](Q179-dmz-lan-single-vpc-two-subnets.md) |
| 180 | APIs (Enable the Cloud Spanner API) | — | A | ❓ Didn't know | [Q180-first-step-enable-spanner-api.md](Q180-first-step-enable-spanner-api.md) |
| 181 | APIs (Enable compute.googleapis.com) | — | C | ❓ Didn't know | [Q181-cli-new-project-enable-compute-api.md](Q181-cli-new-project-enable-compute-api.md) |
| 182 | GKE (Node Pool Autoscaling With Min/Max) | — | C | ❓ Didn't know | [Q182-gke-node-pool-autoscaling-min-max.md](Q182-gke-node-pool-autoscaling-min-max.md) |
| 183 | IAM (New Service Account for It + Storage Permissions) | — | C | ❓ Didn't know | [Q183-new-sa-only-this-vm-reads-files.md](Q183-new-sa-only-this-vm-reads-files.md) |
| 184 | Cloud Storage (Regional Standard) | — | B | ❓ Didn't know | [Q184-mission-critical-analytics-storage-class.md](Q184-mission-critical-analytics-storage-class.md) |
| 185 | App Engine (App Engine New Version + Traffic Splitting) | — | A | ❓ Didn't know | [Q185-app-engine-version-traffic-split.md](Q185-app-engine-version-traffic-split.md) |
| 186 | Cloud Identity (Invite Them to Transfer Their Account) | — | A | ❓ Didn't know | [Q186-cloud-identity-conflicting-accounts-transfer.md](Q186-cloud-identity-conflicting-accounts-transfer.md) |
| 187 | Spanner (Alert at 65% High-Priority CPU, Add Nodes) | — | C | ❓ Didn't know | [Q187-spanner-cpu-65-add-nodes.md](Q187-spanner-cpu-65-add-nodes.md) |
| 188 | Databases (Cloud SQL) | — | B | ❓ Didn't know | [Q188-postgres-acid-single-site-cloud-sql.md](Q188-postgres-acid-single-site-cloud-sql.md) |
| 189 | gcloud CLI (gcloud config set container/cluster dev) | — | A | ❓ Didn't know | [Q189-gcloud-config-set-container-cluster.md](Q189-gcloud-config-set-container-cluster.md) |
| 190 | Resource hierarchy (New Project acme-marketing-data-digest) | — | C | ❓ Didn't know | [Q190-separate-project-marketing-team.md](Q190-separate-project-marketing-team.md) |
| 191 | Security (IAP for SSH and TCP) | — | B | ❓ Didn't know | [Q191-ssh-no-public-ip-iap-tcp.md](Q191-ssh-no-public-ip-iap-tcp.md) |
| 192 | GKE (Container Registry + Kubernetes Deployment) | — | D | ❓ Didn't know | [Q192-docker-image-gke-container-registry-deployment.md](Q192-docker-image-gke-container-registry-deployment.md) |
| 193 | BigQuery (Review the Nightly Job in BigQuery) | — | B | ❓ Didn't know | [Q193-data-studio-broken-check-bigquery-job.md](Q193-data-studio-broken-check-bigquery-job.md) |
| 194 | Resource hierarchy (Folders) | — | B | ❓ Didn't know | [Q194-group-common-iam-folders.md](Q194-group-common-iam-folders.md) |
| 195 | Networking (Custom VPC, Cloud Router BGP, Active/Passive) | — | C | ❓ Didn't know | [Q195-ha-vpn-custom-vpc-bgp-active-passive.md](Q195-ha-vpn-custom-vpc-bgp-active-passive.md) |
| 196 | GKE (Compute-Optimized Node Pool for It) | — | B | ❓ Didn't know | [Q196-cpu-heavy-microservice-compute-node-pool.md](Q196-cpu-heavy-microservice-compute-node-pool.md) |
| 197 | Billing (New Project Linked to a Marketing Billing Account) | — | C | ❓ Didn't know | [Q197-bill-marketing-new-project-billing-account.md](Q197-bill-marketing-new-project-billing-account.md) |
| 198 | Load balancing (External TCP Network Load Balancer) | — | A | ❓ Didn't know | [Q198-tcp-389-preserve-client-ip-network-lb.md](Q198-tcp-389-preserve-client-ip-network-lb.md) |
| 199 | Databases (Cloud Spanner) | — | B | ❓ Didn't know | [Q199-global-game-db-spanner.md](Q199-global-game-db-spanner.md) |
| 200 | Databases (Cloud Spanner) | — | C | ❓ Didn't know | [Q200-global-relational-unknown-scale-spanner.md](Q200-global-relational-unknown-scale-spanner.md) |
| 201 | Billing (Billing Export to BigQuery + Looker Studio) | — | D | ❓ Didn't know | [Q201-custom-cost-metrics-bigquery-export-looker.md](Q201-custom-cost-metrics-bigquery-export-looker.md) |
| 202 | Networking (Enable Private Google Access on the Subnet) | — | C | ❓ Didn't know | [Q202-internal-only-vm-gcs-private-google-access.md](Q202-internal-only-vm-gcs-private-google-access.md) |
| 203 | Resource hierarchy (projects.move + Change Billing Account) | — | A | ❓ Didn't know | [Q203-move-acquired-project-projects-move.md](Q203-move-acquired-project-projects-move.md) |
| 204 | Organization Policy (Folder + Organization Policy on Locations) | — | A | ❓ Didn't know | [Q204-restrict-dev-resources-us-org-policy.md](Q204-restrict-dev-resources-us-org-policy.md) |
| 205 | Networking (One A Record + Two CNAMEs) | — | C | ❓ Didn't know | [Q205-cloud-dns-a-record-cname.md](Q205-cloud-dns-a-record-cname.md) |
| 206 | Networking (Ingress Rule: Source SA sa-app → Target SA sa-db) | — | A | ❓ Didn't know | [Q206-firewall-sa-app-to-sa-db.md](Q206-firewall-sa-app-to-sa-db.md) |
| 207 | Marketplace (Deploy Directly From Cloud Marketplace) | — | B | ❓ Didn't know | [Q207-cms-deploy-directly-marketplace.md](Q207-cms-deploy-directly-marketplace.md) |
| 208 | Billing (One Billing Account + Billing Account User for Creators) | — | A | ❓ Didn't know | [Q208-engineers-create-projects-shared-billing-account.md](Q208-engineers-create-projects-shared-billing-account.md) |
| 209 | IAM (IAM Roles at the Project + Inherited) | — | A | ❓ Didn't know | [Q209-cicd-sa-check-iam-roles-inherited.md](Q209-cicd-sa-check-iam-roles-inherited.md) |
| 210 | Security (gcloud compute ssh --tunnel-through-iap + Allow 35.235.240.0/20) | — | B | ❓ Didn't know | [Q210-secure-cheap-ssh-iap-tunnel.md](Q210-secure-cheap-ssh-iap-tunnel.md) |
| 211 | IAM (Custom Role With Exactly Those Permissions) | — | A | ❓ Didn't know | [Q211-external-user-list-images-disks-custom-role.md](Q211-external-user-list-images-disks-custom-role.md) |
| 212 | Cloud Run (Cold Starts: Set Minimum Instances) | — | A | ❓ Didn't know | [Q212-cloud-run-cold-start-min-instances.md](Q212-cloud-run-cold-start-min-instances.md) |
| 213 | Data pipelines (Pub/Sub → Dataflow → Cloud Storage) | — | A | ❓ Didn't know | [Q213-iot-data-lake-pubsub-dataflow-gcs.md](Q213-iot-data-lake-pubsub-dataflow-gcs.md) |
| 214 | Networking (Expand It to 10.0.0.0/18) | — | B | ❓ Didn't know | [Q214-subnet-out-of-ips-expand-to-18.md](Q214-subnet-out-of-ips-expand-to-18.md) |
| 215 | IAM (Group + Org-Level Custom Role) | — | D | ❓ Didn't know | [Q215-same-dev-permissions-org-custom-role-group.md](Q215-same-dev-permissions-org-custom-role-group.md) |
| 216 | Data transfer (gcloud storage Sync Script on a Cron Schedule) | — | B | ❓ Didn't know | [Q216-onprem-images-gcloud-storage-rsync-cron.md](Q216-onprem-images-gcloud-storage-rsync-cron.md) |
| 217 | Databases (Cloud SQL) | — | C | ❓ Didn't know | [Q217-postgres-acid-single-site-cloud-sql-v2.md](Q217-postgres-acid-single-site-cloud-sql-v2.md) |
| 218 | Compute Engine (Regular VM, Start and Stop as Needed) | — | B | ❓ Didn't know | [Q218-monthly-30h-batch-regular-vm-v2.md](Q218-monthly-30h-batch-regular-vm-v2.md) |
| 219 | Migration (Spanner, Pub/Sub, BigQuery) | — | B | ❓ Didn't know | [Q219-migrate-mysql-kafka-postgres-spanner-pubsub-bq.md](Q219-migrate-mysql-kafka-postgres-spanner-pubsub-bq.md) |
| 220 | Organization Policy (Domain Restriction Org Policy + Remove Existing Users) | — | D | ❓ Didn't know | [Q220-domain-restricted-sharing-remove-existing.md](Q220-domain-restricted-sharing-remove-existing.md) |
| 221 | Compute Engine (gcloud compute instance-groups managed recreate-instances) | — | B | ❓ Didn't know | [Q221-mig-replace-one-vm-recreate-instances.md](Q221-mig-replace-one-vm-recreate-instances.md) |
| 222 | Config Connector (kubectl delete the Resource) | — | B | ❓ Didn't know | [Q222-config-connector-delete-kubectl.md](Q222-config-connector-delete-kubectl.md) |
| 223 | Cloud Identity (Cloud Identity Groups + Enforce MFA) | — | B | ❓ Didn't know | [Q223-scale-identity-groups-mfa.md](Q223-scale-identity-groups-mfa.md) |
| 224 | Compute Engine (Instance Group + CPU Autoscaling) | — | D | ❓ Didn't know | [Q224-video-encoding-mig-cpu-autoscaling.md](Q224-video-encoding-mig-cpu-autoscaling.md) |
| 225 | Compute Engine (New Valid Template + Delete Disks With Conflicting Names) | — | A | ❓ Didn't know | [Q225-mig-creation-failed-template-disk-names.md](Q225-mig-creation-failed-template-disk-names.md) |
| 226 | GKE (Artifact Registry + Kubernetes Deployment) | — | D | ❓ Didn't know | [Q226-docker-image-gke-artifact-registry-deployment.md](Q226-docker-image-gke-artifact-registry-deployment.md) |
| 227 | BigQuery (Review the Nightly Job in BigQuery) | — | D | ❓ Didn't know | [Q227-looker-studio-broken-check-bigquery-job.md](Q227-looker-studio-broken-check-bigquery-job.md) |
| 228 | Compute Engine (Test With Simulated Maintenance, Then Use Spot N2 VMs) | — | A | ❓ Didn't know | [Q228-fault-tolerant-batch-spot-n2.md](Q228-fault-tolerant-batch-spot-n2.md) |
| 229 | Billing (Billing Export to BigQuery + Looker Studio) | — | D | ❓ Didn't know | [Q229-multi-billing-single-view-bq-export-looker.md](Q229-multi-billing-single-view-bq-export-looker.md) |
| 230 | Cloud Storage (Upload to Cloud Storage With gcloud storage) | — | B | ❓ Didn't know | [Q230-unstructured-etl-dataflow-cloud-storage.md](Q230-unstructured-etl-dataflow-cloud-storage.md) |
| 231 | Logging (Install the Ops Agent, View in Cloud Logging) | — | D | ❓ Didn't know | [Q231-logs-on-disk-ops-agent.md](Q231-logs-on-disk-ops-agent.md) |
| 232 | APIs (Enable compute and storage APIs With gcloud services enable) | — | B | ❓ Didn't know | [Q232-enable-compute-and-storage-apis.md](Q232-enable-compute-and-storage-apis.md) |
| 233 | Serverless (Artifact Registry + Cloud Run) | — | D | ❓ Didn't know | [Q233-containers-no-infra-autoscale-cloud-run.md](Q233-containers-no-infra-autoscale-cloud-run.md) |
| 234 | Compute Engine (Regional Persistent Disk, Attach to an Instance in the Other Zone) | — | D | ❓ Didn't know | [Q234-zonal-failure-regional-pd-attach.md](Q234-zonal-failure-regional-pd-attach.md) |
| 235 | IAM (Viewer + Compute Admin) | — | A | ❓ Didn't know | [Q235-devops-compute-admin-plus-viewer.md](Q235-devops-compute-admin-plus-viewer.md) |
| 236 | Serverless (Existing CI/CD, Deploy Images to Cloud Run, Update Config) | — | A | ❓ Didn't know | [Q236-python-microservices-serverless-cloud-run.md](Q236-python-microservices-serverless-cloud-run.md) |
| 237 | GKE (Compute-Optimized Node Pool for It) | — | B | ❓ Didn't know | [Q237-cpu-heavy-microservice-compute-node-pool-n2.md](Q237-cpu-heavy-microservice-compute-node-pool-n2.md) |
| 238 | GKE (GKE Autopilot + Stable Release Channel) | — | B | ❓ Didn't know | [Q238-reliable-k8s-autopilot-stable-channel.md](Q238-reliable-k8s-autopilot-stable-channel.md) |
| 239 | Monitoring (Cloud Monitoring Alert Policy) | — | B | ❓ Didn't know | [Q239-latency-5-min-alert-policy.md](Q239-latency-5-min-alert-policy.md) |
| 240 | Serverless (Container + Cloud Scheduler → Cloud Run Job) | — | A | ❓ Didn't know | [Q240-midnight-binaries-cloud-run-job.md](Q240-midnight-binaries-cloud-run-job.md) |
