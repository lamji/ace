# ACE Exam Review Index

**Score: 35 / 375 (9%)**: 26 incorrect, 314 didn't know

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
| 45 | App Engine (roll back: route 100% traffic to previous version) | — | C | ❓ Didn't know | [Q045-app-engine-rollback-traffic.md](Q045-app-engine-rollback-traffic.md) |
| 46 | App Engine + gcloud CLI (active project configuration vs app.yaml) | A | D | ❌ | [Q046-app-engine-gcloud-project-config.md](Q046-app-engine-gcloud-project-config.md) |
| 47 | Compute Engine (instance template, automatic restart, host maintenance migration vs autohealing) | C | A | ❌ | [Q047-compute-engine-maintenance-restart.md](Q047-compute-engine-maintenance-restart.md) |
| 48 | Cloud Storage (PDF object Content-Type vs public access, CDN, bucket labels) | B | C | ❌ | [Q048-cloud-storage-pdf-content-type.md](Q048-cloud-storage-pdf-content-type.md) |
| 49 | Compute Engine (stop → increase memory / custom machine type → start) | D | D | ✅ | [Q049-vm-increase-memory.md](Q049-vm-increase-memory.md) |
| 50 | VPC networking (one VPC, 2 subnets, non-overlapping CIDR; VPC global) | B | A | ❌ | [Q050-vpc-two-subnets-prod-test.md](Q050-vpc-two-subnets-prod-test.md) |
| 51 | Compute Engine (MIG autohealing: HTTPS health check on port 443) | — | A | ❓ Didn't know | [Q051-mig-https-health-check-autohealing.md](Q051-mig-https-health-check-autohealing.md) |
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
| 241 | GKE (gcloud container clusters get-credentials dev-cluster) | — | A | ❓ Didn't know | [Q241-kubectl-switch-cluster-get-credentials.md](Q241-kubectl-switch-cluster-get-credentials.md) |
| 242 | Organization Policy (Org Policies: Key Expiry 24h + Deny Key Creation Except pj-sa) | — | C | ❓ Didn't know | [Q242-sa-keys-24h-org-policies.md](Q242-sa-keys-24h-org-policies.md) |
| 243 | Billing (Pricing Calculator per Resource) | — | D | ❓ Didn't know | [Q243-estimate-cost-pricing-calculator.md](Q243-estimate-cost-pricing-calculator.md) |
| 244 | Logging (Data Read/Write + Admin Read Logs, Sink to Pub/Sub) | — | C | ❓ Didn't know | [Q244-bigtable-pii-audit-logs-pubsub-siem.md](Q244-bigtable-pii-audit-logs-pubsub-siem.md) |
| 245 | GKE (Private Autopilot Cluster) | — | A | ❓ Didn't know | [Q245-gke-private-autopilot.md](Q245-gke-private-autopilot.md) |
| 246 | Serverless (App Engine, Cloud Run, Cloud Tasks → Cloud Run) | — | B | ❓ Didn't know | [Q246-serverless-flask-api-job-appengine-cloudrun.md](Q246-serverless-flask-api-job-appengine-cloudrun.md) |
| 247 | IAM (One SA per Pipeline, Keys in Secret Manager) | — | D | ❓ Didn't know | [Q247-cicd-pipeline-per-pipeline-sa-secrets.md](Q247-cicd-pipeline-per-pipeline-sa-secrets.md) |
| 248 | Cloud Storage (Lifecycle Rule → Archive After 30 Days) | — | A | ❓ Didn't know | [Q248-lifecycle-archive-after-30-days.md](Q248-lifecycle-archive-after-30-days.md) |
| 249 | GKE (HPA for Availability, VPA Recommendations for Suggestions) | — | B | ❓ Didn't know | [Q249-unknown-resources-hpa-vpa-recommendations.md](Q249-unknown-resources-hpa-vpa-recommendations.md) |
| 250 | Cloud Storage (Object Versioning + Lifecycle Rules) | — | D | ❓ Didn't know | [Q250-invoices-versioning-lifecycle.md](Q250-invoices-versioning-lifecycle.md) |
| 251 | gcloud CLI (Set CLOUDSDK_PROXY_USERNAME/PASSWORD as Environment Variables) | — | D | ❓ Didn't know | [Q251-gcloud-proxy-credentials-env-vars.md](Q251-gcloud-proxy-credentials-env-vars.md) |
| 252 | GKE (Spot Pool for Fault-Tolerant, Standard Pool for Critical) | — | D | ❓ Didn't know | [Q252-gke-spot-pool-fault-tolerant-standard-critical.md](Q252-gke-spot-pool-fault-tolerant-standard-critical.md) |
| 253 | Cloud Run (Cloud Run Gradual Rollouts) | — | A | ❓ Didn't know | [Q253-serverless-canary-cloud-run-gradual-rollout.md](Q253-serverless-canary-cloud-run-gradual-rollout.md) |
| 254 | Compute Engine (OS Config Agent + roles/osconfig.vulnerabilityReportViewer) | — | C | ❓ Didn't know | [Q254-vulnerability-report-viewer-os-config.md](Q254-vulnerability-report-viewer-os-config.md) |
| 255 | Cloud Run (Gradual Rollout, Split Traffic Between Revisions) | — | B | ❓ Didn't know | [Q255-cloud-run-gradual-rollout-limit-impact.md](Q255-cloud-run-gradual-rollout-limit-impact.md) |
| 256 | Compute Engine (Their Public Key Added to the VM) | — | C | ❓ Didn't know | [Q256-consultant-no-google-account-ssh-public-key.md](Q256-consultant-no-google-account-ssh-public-key.md) |
| 257 | Monitoring (Log-Based Metrics + Alerts) | — | B | ❓ Didn't know | [Q257-monitor-firewall-instance-changes-log-metrics.md](Q257-monitor-firewall-instance-changes-log-metrics.md) |
| 258 | IAM (bigquery.dataViewer on crm-databases) | — | D | ❓ Didn't know | [Q258-cross-project-bigquery-dataviewer.md](Q258-cross-project-bigquery-dataviewer.md) |
| 259 | Networking (Expand the Subnet to 172.16.20.0/24) | — | A | ❓ Didn't know | [Q259-dataproc-subnet-full-expand-24.md](Q259-dataproc-subnet-full-expand-24.md) |
| 260 | Databases (Multi-Region Cloud Spanner) | — | A | ❓ Didn't know | [Q260-global-transactions-sql-spanner.md](Q260-global-transactions-sql-spanner.md) |
| 261 | IAM (gcloud iam roles copy to the Startup's Org ID) | — | C | ❓ Didn't know | [Q261-copy-custom-role-to-other-org.md](Q261-copy-custom-role-to-other-org.md) |
| 262 | Serverless (Cloud Function With a Cloud Storage Trigger) | — | D | ❓ Didn't know | [Q262-speech-to-text-function-gcs-trigger.md](Q262-speech-to-text-function-gcs-trigger.md) |
| 263 | Load balancing (External HTTPS LB, Managed Cert, URL Map to Bucket Backend) | — | A | ❓ Didn't know | [Q263-secure-autoscaled-site-https-lb-url-map-bucket.md](Q263-secure-autoscaled-site-https-lb-url-map-bucket.md) |
| 264 | Databases (Bigtable, Timestamp Row Key) | — | D | ❓ Didn't know | [Q264-sensor-events-bigtable-timestamp.md](Q264-sensor-events-bigtable-timestamp.md) |
| 265 | gcloud CLI (gcloud auth login + gcloud config set project) | — | A, E | ❓ Didn't know | [Q265-new-laptop-gcloud-auth-login-set-project.md](Q265-new-laptop-gcloud-auth-login-set-project.md) |
| 266 | Migration (Transfer Appliance, BigQuery Data Transfer Service, Storage Transfer Service) | — | B | ❓ Didn't know | [Q266-migrate-transfer-appliance-bq-dts-sts.md](Q266-migrate-transfer-appliance-bq-dts-sts.md) |
| 267 | GKE (GKE Autopilot) | — | A | ❓ Didn't know | [Q267-k8s-manifest-full-control-autopilot.md](Q267-k8s-manifest-full-control-autopilot.md) |
| 268 | Serverless (Pub/Sub → Cloud Functions) | — | D | ❓ Didn't know | [Q268-votes-pubsub-cloud-functions.md](Q268-votes-pubsub-cloud-functions.md) |
| 269 | Cloud SQL (Cloud SQL IAM Auth + Cloud SQL Auth Proxy) | — | C | ❓ Didn't know | [Q269-cloud-sql-iam-auth-proxy.md](Q269-cloud-sql-iam-auth-proxy.md) |
| 270 | Networking (VPC Network Peering) | — | B | ❓ Didn't know | [Q270-two-projects-vpc-peering.md](Q270-two-projects-vpc-peering.md) |
| 271 | Compute Engine (Scheduled Snapshots With 7-Day Retention) | — | B | ❓ Didn't know | [Q271-daily-snapshot-schedule-7-days.md](Q271-daily-snapshot-schedule-7-days.md) |
| 272 | Infrastructure as Code (Terraform Modules in a Repository) | — | D | ❓ Didn't know | [Q272-approved-config-terraform-modules.md](Q272-approved-config-terraform-modules.md) |
| 273 | Resource hierarchy (Folders per Department, Set Both on Folders) | — | C | ❓ Didn't know | [Q273-dept-folders-org-policies-log-sinks.md](Q273-dept-folders-org-policies-log-sinks.md) |
| 274 | Load balancing + Cloud DNS (HTTP(S) Load Balancing + A Record in a Public DNS Zone) | — | D | ❓ Didn't know | [Q274-mig-secure-ha-https-lb-a-record.md](Q274-mig-secure-ha-https-lb-a-record.md) |
| 275 | GKE (Vertical Pod Autoscaler per Microservice) | — | A | ❓ Didn't know | [Q275-right-size-limits-vpa.md](Q275-right-size-limits-vpa.md) |
| 276 | BigQuery (INFORMATION_SCHEMA Views + Cloud Audit Logs) | — | B, D | ❓ Didn't know | [Q276-bigquery-quota-exceeded-info-schema-audit-logs.md](Q276-bigquery-quota-exceeded-info-schema-audit-logs.md) |
| 277 | Compute Engine (Managed Instance Group + Autoscaling) | — | A | ❓ Didn't know | [Q277-stateless-vm-app-mig-autoscaling.md](Q277-stateless-vm-app-mig-autoscaling.md) |
| 278 | Cloud Run (Lower the Maximum Number of Cloud Run Instances) | — | C | ❓ Didn't know | [Q278-cloud-run-cloud-sql-quota-max-instances.md](Q278-cloud-run-cloud-sql-quota-max-instances.md) |
| 279 | Cloud Run (Cloud Run With Private Service Connect) | — | C | ❓ Didn't know | [Q279-internal-web-app-cloud-run-psc.md](Q279-internal-web-app-cloud-run-psc.md) |
| 280 | Logging (Enable Log Analytics on the Log Bucket + Linked BigQuery Dataset) | — | B | ❓ Didn't know | [Q280-sql-on-logs-log-analytics.md](Q280-sql-on-logs-log-analytics.md) |
| 281 | Compute Engine (Hyperdisk Extreme in a Stateful MIG) | — | C | ❓ Didn't know | [Q281-fastest-disk-recover-hyperdisk-stateful-mig.md](Q281-fastest-disk-recover-hyperdisk-stateful-mig.md) |
| 282 | Networking (Promote Its IP to a Static Internal IP) | — | B | ❓ Didn't know | [Q282-fixed-internal-ip-promote-static.md](Q282-fixed-internal-ip-promote-static.md) |
| 283 | GKE (Create an Autopilot Cluster) | — | B | ❓ Didn't know | [Q283-preview-to-ga-autopilot.md](Q283-preview-to-ga-autopilot.md) |
| 284 | IAM (gcloud Service Account Impersonation) | — | C | ❓ Didn't know | [Q284-test-sa-permissions-impersonation.md](Q284-test-sa-permissions-impersonation.md) |
| 285 | IAM + Organization Policy (Groups + IAM Roles + Org Policy Blocking Other Domains) | — | B | ❓ Didn't know | [Q285-company-accounts-groups-iam-domain-policy.md](Q285-company-accounts-groups-iam-domain-policy.md) |
| 286 | Networking (Internal Application LB + Cloud DNS + Serverless VPC Access Connector) | — | D | ❓ Didn't know | [Q286-cloud-run-to-gke-api-internal-lb-vpc-connector.md](Q286-cloud-run-to-gke-api-internal-lb-vpc-connector.md) |
| 287 | Logging (Log Sink to Pub/Sub, SaaS Subscribes) | — | B | ❓ Didn't know | [Q287-logs-to-saas-sink-pubsub.md](Q287-logs-to-saas-sink-pubsub.md) |
| 288 | GKE (StatefulSet + Cluster Autoscaling) | — | A | ❓ Didn't know | [Q288-gke-database-statefulset-cluster-autoscaler.md](Q288-gke-database-statefulset-cluster-autoscaler.md) |
| 289 | Cloud Storage (Versioning + Pub/Sub Notifications for Cloud Storage) | — | B | ❓ Didn't know | [Q289-notify-gcs-changes-pubsub-notifications.md](Q289-notify-gcs-changes-pubsub-notifications.md) |
| 290 | Cloud Storage (Cloud Storage Lifecycle → Coldline After 6 Months) | — | A | ❓ Didn't know | [Q290-invoices-3-years-lifecycle-coldline.md](Q290-invoices-3-years-lifecycle-coldline.md) |
| 291 | GKE (Autopilot) | — | D | ❓ Didn't know | [Q291-gke-ha-no-node-mgmt-autopilot.md](Q291-gke-ha-no-node-mgmt-autopilot.md) |
| 292 | Storage choice (Cloud SQL, Cloud Storage Archive, Bigtable) | — | C | ❓ Didn't know | [Q292-mixed-data-cloudsql-archive-bigtable.md](Q292-mixed-data-cloudsql-archive-bigtable.md) |
| 293 | Networking (Premium Tier for Prod, Standard Tier for Dev) | — | B | ❓ Didn't know | [Q293-prod-premium-dev-standard-tier.md](Q293-prod-premium-dev-standard-tier.md) |
| 294 | Compute Engine (OS Login + Google Group) | — | D | ❓ Didn't know | [Q294-ssh-team-oslogin-group.md](Q294-ssh-team-oslogin-group.md) |
| 295 | Monitoring (Cloud Monitoring Alert on Data Freshness) | — | B | ❓ Didn't know | [Q295-dataflow-stuck-data-freshness-alert.md](Q295-dataflow-stuck-data-freshness-alert.md) |
| 296 | GKE (GKE Autopilot) | — | A | ❓ Didn't know | [Q296-private-microservices-gke-autopilot.md](Q296-private-microservices-gke-autopilot.md) |
| 297 | IAM (Custom SA, Data Viewer on the Dataset) | — | B | ❓ Didn't know | [Q297-vm-bigquery-dataset-custom-sa.md](Q297-vm-bigquery-dataset-custom-sa.md) |
| 298 | Serverless (Pub/Sub + Cloud Run) | — | C | ❓ Didn't know | [Q298-async-transactions-pubsub-cloud-run.md](Q298-async-transactions-pubsub-cloud-run.md) |
| 299 | Storage (Filestore) | — | B | ❓ Didn't know | [Q299-nfs-modernize-filestore.md](Q299-nfs-modernize-filestore.md) |
| 300 | Logging (Ops Agent + Log Analytics) | — | C | ❓ Didn't know | [Q300-vm-logs-ops-agent-log-analytics.md](Q300-vm-logs-ops-agent-log-analytics.md) |
| 301 | GKE security (Workload Identity Federation for GKE) | — | B | ❓ Didn't know | [Q301-gke-pods-gcs-no-keys-workload-identity.md](Q301-gke-pods-gcs-no-keys-workload-identity.md) |
| 302 | Compute Engine (OS Login + IAM Roles) | — | A | ❓ Didn't know | [Q302-linux-account-lifecycle-oslogin-iam.md](Q302-linux-account-lifecycle-oslogin-iam.md) |
| 303 | IAM (Custom Role With Only the Required Permissions) | — | C | ❓ Didn't know | [Q303-ops-team-custom-role-only-needed.md](Q303-ops-team-custom-role-only-needed.md) |
| 304 | Infrastructure as Code (Terraform) | — | B | ❓ Didn't know | [Q304-multicloud-iac-terraform.md](Q304-multicloud-iac-terraform.md) |
| 305 | Serverless (Cloud Run + Eventarc) | — | D | ❓ Didn't know | [Q305-events-public-scale-to-zero-cloud-run-eventarc.md](Q305-events-public-scale-to-zero-cloud-run-eventarc.md) |
| 306 | Networking (Same CIDR Ranges, Same Static IPs) | — | C | ❓ Didn't know | [Q306-lift-shift-hardcoded-ips-same-cidr.md](Q306-lift-shift-hardcoded-ips-same-cidr.md) |
| 307 | Compute Engine (Spot VMs) | — | C | ❓ Didn't know | [Q307-nightly-batch-interruptible-spot.md](Q307-nightly-batch-interruptible-spot.md) |
| 308 | Databases (Spanner) | — | B | ❓ Didn't know | [Q308-growing-postgres-multiregion-spanner.md](Q308-growing-postgres-multiregion-spanner.md) |
| 309 | Billing (Enable Billing Export to BigQuery) | — | A | ❓ Didn't know | [Q309-billing-export-bigquery.md](Q309-billing-export-bigquery.md) |
| 310 | Serverless (Cloud Run Job + Cloud Scheduler) | — | C | ❓ Didn't know | [Q310-overnight-batch-retry-cloud-run-job.md](Q310-overnight-batch-retry-cloud-run-job.md) |
| 311 | Databases (AlloyDB) | — | A | ❓ Didn't know | [Q311-postgres-150tb-performance-alloydb.md](Q311-postgres-150tb-performance-alloydb.md) |
| 312 | AI/ML infrastructure (GKE + Hardware Accelerators) | — | D | ❓ Didn't know | [Q312-llm-finetune-gke-accelerators.md](Q312-llm-finetune-gke-accelerators.md) |
| 313 | GKE (kubectl rollout undo) | — | C | ❓ Didn't know | [Q313-gke-rollback-rollout-undo.md](Q313-gke-rollback-rollout-undo.md) |
| 314 | Networking (Private Nodes + Cloud NAT With Static IPs) | — | B | ❓ Didn't know | [Q314-gke-vendor-allowlist-cloud-nat-static.md](Q314-gke-vendor-allowlist-cloud-nat-static.md) |
| 315 | Serverless (Both on Cloud Run) | — | C | ❓ Didn't know | [Q315-static-site-and-http-job-cloud-run.md](Q315-static-site-and-http-job-cloud-run.md) |
| 316 | Billing (Folder + Budget Scoped to Folder) | — | B | ❓ Didn't know | [Q316-sandbox-folder-budget-alert.md](Q316-sandbox-folder-budget-alert.md) |
| 317 | Networking (Shared VPC + Hierarchical Firewall Policies) | — | D | ❓ Didn't know | [Q317-landing-zone-shared-vpc-hierarchical-fw.md](Q317-landing-zone-shared-vpc-hierarchical-fw.md) |
| 318 | Infrastructure as Code (Compliant Terraform Modules) | — | C | ❓ Didn't know | [Q318-compliant-terraform-modules.md](Q318-compliant-terraform-modules.md) |
| 319 | Cloud Run (Revision Min Instances = 2) | — | C | ❓ Didn't know | [Q319-cloud-run-revision-min-instances.md](Q319-cloud-run-revision-min-instances.md) |
| 320 | GKE (Vertical Pod Autoscaler) | — | B | ❓ Didn't know | [Q320-single-replica-more-cpu-vpa.md](Q320-single-replica-more-cpu-vpa.md) |
| 321 | Billing (Billing Export to BigQuery + Looker Studio) | — | B | ❓ Didn't know | [Q321-cost-analysis-billing-export-looker-studio.md](Q321-cost-analysis-billing-export-looker-studio.md) |
| 322 | Data transfer (Storage Transfer Service) | — | A | ❓ Didn't know | [Q322-migrate-150tb-video-storage-transfer-service.md](Q322-migrate-150tb-video-storage-transfer-service.md) |
| 323 | Compute Engine (Enforce OS Login via Organization Policy) | — | C | ❓ Didn't know | [Q323-company-ssh-standard-oslogin-org-policy.md](Q323-company-ssh-standard-oslogin-org-policy.md) |
| 324 | Databases (Bigtable) | — | B | ❓ Didn't know | [Q324-iot-submillisecond-bigtable.md](Q324-iot-submillisecond-bigtable.md) |
| 325 | Pub/Sub (gcloud pubsub subscriptions pull --auto-ack) | — | C | ❓ Didn't know | [Q325-pubsub-pull-auto-ack.md](Q325-pubsub-pull-auto-ack.md) |
| 326 | IAM (Single-Purpose Service Accounts + Manage Them as Resources) | — | C, D | ❓ Didn't know | [Q326-service-account-best-practices-two.md](Q326-service-account-best-practices-two.md) |
| 327 | Databases (Spanner) | — | B | ❓ Didn't know | [Q327-global-relational-scale-spanner.md](Q327-global-relational-scale-spanner.md) |
| 328 | Troubleshooting (Review the Error Message) | — | D | ❓ Didn't know | [Q328-troubleshoot-review-error-first.md](Q328-troubleshoot-review-error-first.md) |
| 329 | Networking (Expand the Primary IP Range) | — | D | ❓ Didn't know | [Q329-subnet-full-expand-range.md](Q329-subnet-full-expand-range.md) |
| 330 | Serverless (Cloud Run Service) | — | C | ❓ Didn't know | [Q330-unpredictable-web-cloud-run-service.md](Q330-unpredictable-web-cloud-run-service.md) |
| 331 | Networking (Multi-Region VMs + Global External Application Load Balancer) | — | B, D | ❓ Didn't know | [Q331-global-website-multiregion-global-alb.md](Q331-global-website-multiregion-global-alb.md) |
| 332 | IAM (Impersonation + gcloud config set) | — | B | ❓ Didn't know | [Q332-local-script-sa-impersonation.md](Q332-local-script-sa-impersonation.md) |
| 333 | Organization Policy (Resource Locations Constraint at Org Level With Allowed Locations) | — | B | ❓ Didn't know | [Q333-eea-resource-locations-org-allowed.md](Q333-eea-resource-locations-org-allowed.md) |
| 334 | Networking (One /16 Custom VPC, Three Subnets, Subnet-Based Firewall Rules) | — | B | ❓ Didn't know | [Q334-three-tier-one-vpc-three-subnets.md](Q334-three-tier-one-vpc-three-subnets.md) |
| 335 | Billing (Budget Alerts + Billing Export to BigQuery) | — | D | ❓ Didn't know | [Q335-team-cost-alerts-billing-export.md](Q335-team-cost-alerts-billing-export.md) |
| 336 | Databases (AlloyDB via Database Migration Service) | — | C | ❓ Didn't know | [Q336-postgres-demanding-alloydb-dms.md](Q336-postgres-demanding-alloydb-dms.md) |
| 337 | Identity (Google Cloud Directory Sync) | — | D | ❓ Didn't know | [Q337-ldap-ou-sync-gcds.md](Q337-ldap-ou-sync-gcds.md) |
| 338 | GKE (GKE Standard Fixed Node Pool + Cloud Service Mesh) | — | D | ❓ Didn't know | [Q338-mesh-fixed-instances-gke-standard.md](Q338-mesh-fixed-instances-gke-standard.md) |
| 339 | Networking (Cloud DNS Private Zone) | — | B | ❓ Didn't know | [Q339-internal-domain-cloud-dns-private-zone.md](Q339-internal-domain-cloud-dns-private-zone.md) |
| 340 | Security (gcloud asset search-all-resources for ServiceAccountKey) | — | D | ❓ Didn't know | [Q340-audit-old-sa-keys-asset-search.md](Q340-audit-old-sa-keys-asset-search.md) |
| 341 | Infrastructure as Code (Cloud Storage Backend) | — | B | ❓ Didn't know | [Q341-terraform-gcs-backend.md](Q341-terraform-gcs-backend.md) |
| 342 | Resource hierarchy & Billing (One Org, a Folder per Startup, Separate Billing Accounts) | — | B | ❓ Didn't know | [Q342-startups-folders-separate-billing.md](Q342-startups-folders-separate-billing.md) |
| 343 | Logging (Explain This Log Entry with Gemini in Logs Explorer) | — | C | ❓ Didn't know | [Q343-cryptic-logs-gemini-explain.md](Q343-cryptic-logs-gemini-explain.md) |
| 344 | Logging (Log View + logging.viewAccessor) | — | D | ❓ Didn't know | [Q344-log-view-view-accessor.md](Q344-log-view-view-accessor.md) |
| 345 | IAM (roles/iam.serviceAccountAdmin) | — | A | ❓ Didn't know | [Q345-modify-sa-iam-policy-sa-admin.md](Q345-modify-sa-iam-policy-sa-admin.md) |
| 346 | IAM (Storage Object Viewer on the Bucket) | — | D | ❓ Didn't know | [Q346-vendor-read-bucket-object-viewer.md](Q346-vendor-read-bucket-object-viewer.md) |
| 347 | IAM (Custom Role With Exactly Those Permissions) | — | C | ❓ Didn't know | [Q347-ops-start-stop-reset-custom-role.md](Q347-ops-start-stop-reset-custom-role.md) |
| 348 | Security (Cloud Asset Inventory) | — | C | ❓ Didn't know | [Q348-public-ip-audit-asset-inventory.md](Q348-public-ip-audit-asset-inventory.md) |
| 349 | Resource Manager / IAM (Check the Owner Role on the IAM Page) | — | D | ❓ Didn't know | [Q349-project-creator-owner-role.md](Q349-project-creator-owner-role.md) |
| 350 | Organization Policy / IAM (Folder + Org Policy Locations & Services + Owner) | — | A | ❓ Didn't know | [Q350-ds-sandbox-folder-orgpolicy-owner.md](Q350-ds-sandbox-folder-orgpolicy-owner.md) |
| 351 | Networking (Cloud NAT) | — | D | ❓ Didn't know | [Q351-no-external-ip-internet-cloud-nat.md](Q351-no-external-ip-internet-cloud-nat.md) |
| 352 | GKE (gcloud services enable container.googleapis.com) | — | D | ❓ Didn't know | [Q352-gke-api-disabled-enable-container.md](Q352-gke-api-disabled-enable-container.md) |
| 353 | Billing (Standard + Detailed Usage Cost Export) | — | B | ❓ Didn't know | [Q353-billing-standard-detailed-export.md](Q353-billing-standard-detailed-export.md) |
| 354 | GKE (Create Nodes With That Service Account) | — | C | ❓ Didn't know | [Q354-gke-nodes-custom-sa-pull-images.md](Q354-gke-nodes-custom-sa-pull-images.md) |
| 355 | Databases (Database Center) | — | D | ❓ Didn't know | [Q355-db-fleet-health-database-center.md](Q355-db-fleet-health-database-center.md) |
| 356 | Cloud Storage (Uniform Access + IAM Condition on the Prefix) | — | D | ❓ Didn't know | [Q356-prefix-access-ubla-iam-condition.md](Q356-prefix-access-ubla-iam-condition.md) |
| 357 | IAM (Grant Roles to the Agent's Service Account) | — | A | ❓ Didn't know | [Q357-vertex-agent-sa-pubsub-roles.md](Q357-vertex-agent-sa-pubsub-roles.md) |
| 358 | IAM (serviceAccountTokenCreator) | — | C | ❓ Didn't know | [Q358-test-sa-permissions-token-creator.md](Q358-test-sa-permissions-token-creator.md) |
| 359 | BigQuery (Cloud Storage + Partitioned External Table) | — | C | ❓ Didn't know | [Q359-avro-petabytes-external-table.md](Q359-avro-petabytes-external-table.md) |
| 360 | GKE security (Workload Identity Federation) | — | D | ❓ Didn't know | [Q360-gke-monitoring-no-keys-workload-identity.md](Q360-gke-monitoring-no-keys-workload-identity.md) |
| 361 | IAM (Add to Group With container.developer) | — | A | ❓ Didn't know | [Q361-dev-deploy-gke-group-container-developer.md](Q361-dev-deploy-gke-group-container-developer.md) |
| 362 | IAM (Google Groups With Security Label) | — | D | ❓ Didn't know | [Q362-team-access-security-groups.md](Q362-team-access-security-groups.md) |
| 363 | Security (asset search-all-resources for ServiceAccountKey) — repeat of Q340) | — | C | ❓ Didn't know | [Q363-audit-old-sa-keys-asset-search-2.md](Q363-audit-old-sa-keys-asset-search-2.md) |
| 364 | Organization Policy (gcp.resourceLocations allowed in:australia-locations) | — | B | ❓ Didn't know | [Q364-australia-locations-allowed-values.md](Q364-australia-locations-allowed-values.md) |
| 365 | IAM (domain:terramearth.com Principal) | — | A | ❓ Didn't know | [Q365-all-employees-domain-principal.md](Q365-all-employees-domain-principal.md) |
| 366 | Infrastructure as Code (Root Directory per Application) | — | B | ❓ Didn't know | [Q366-terraform-root-dir-per-app.md](Q366-terraform-root-dir-per-app.md) |
| 367 | Cloud Storage (Lifecycle Rule age 90 → SetStorageClass Archive) | — | B | ❓ Didn't know | [Q367-lifecycle-age-90-archive.md](Q367-lifecycle-age-90-archive.md) |
| 368 | Monitoring (Log Each Connection + Log-Based Metric) | — | B | ❓ Didn't know | [Q368-track-db-connections-log-metric.md](Q368-track-db-connections-log-metric.md) |
| 369 | IAM (Dedicated SA + objectCreator on That Bucket) | — | A | ❓ Didn't know | [Q369-vm-logs-bucket-object-creator.md](Q369-vm-logs-bucket-object-creator.md) |
| 370 | Billing (Budget → Pub/Sub → Cloud Run Function That Stops the VM) | — | B | ❓ Didn't know | [Q370-budget-stop-vm-pubsub-function.md](Q370-budget-stop-vm-pubsub-function.md) |
| 371 | Monitoring (Monitoring Alerting Policy on cpu/utilization) | — | C | ❓ Didn't know | [Q371-mig-cpu-75-alert-policy.md](Q371-mig-cpu-75-alert-policy.md) |
| 372 | Infrastructure as Code (Config Connector) | — | D | ❓ Didn't know | [Q372-gke-declarative-config-connector.md](Q372-gke-declarative-config-connector.md) |
| 373 | Serverless (Cloud Run) | — | D | ❓ Didn't know | [Q373-container-scale-to-zero-cloud-run.md](Q373-container-scale-to-zero-cloud-run.md) |
| 374 | Billing (Budget → Pub/Sub → Cloud Run Function → Slack) | — | B | ❓ Didn't know | [Q374-budget-slack-pubsub-function.md](Q374-budget-slack-pubsub-function.md) |
| 375 | Compute Engine (Hyperdisk Extreme) | — | A | ❓ Didn't know | [Q375-sap-hana-hyperdisk-extreme.md](Q375-sap-hana-hyperdisk-extreme.md) |

## 📘 Exam guide practice questions (G001–G050)

Written from the official exam guide to cover topics the question site misses. Not counted in the score above. In the quiz, pick **📘 Exam guide topics** to practice only these.

| # | Guide § | Topic | My Answer | Correct | Result | File |
|---|---|---|---|---|---|---|
| G001 | 1.1 | Identity (Workforce Identity Federation) | — | A | ⏳ Not tried yet | [G001-workforce-identity-federation.md](G001-workforce-identity-federation.md) |
| G002 | 2.3 | VPC firewall (Cloud NGFW secure Tags) | — | D | ⏳ Not tried yet | [G002-ngfw-secure-tags.md](G002-ngfw-secure-tags.md) |
| G003 | 3.2 | Cloud Storage (CMEK encryption) | — | C | ⏳ Not tried yet | [G003-cmek-cloud-storage.md](G003-cmek-cloud-storage.md) |
| G004 | 2.2 | Storage (Managed Lustre vs Filestore vs Cloud Storage) | — | D | ⏳ Not tried yet | [G004-managed-lustre-ai-training.md](G004-managed-lustre-ai-training.md) |
| G005 | 2.2 | Storage (NetApp Volumes) | — | C | ⏳ Not tried yet | [G005-netapp-volumes-smb.md](G005-netapp-volumes-smb.md) |
| G006 | 2.1 | Compute Engine (GPUs vs TPUs) | — | A | ⏳ Not tried yet | [G006-gpu-for-cuda.md](G006-gpu-for-cuda.md) |
| G007 | 2.1 | AI/ML infrastructure (TPUs) | — | D | ⏳ Not tried yet | [G007-tpu-large-jax-training.md](G007-tpu-large-jax-training.md) |
| G008 | 2.1 | AI agents (Agent Runtime) | — | A | ⏳ Not tried yet | [G008-agent-runtime-deploy.md](G008-agent-runtime-deploy.md) |
| G009 | 3.1 | AI/ML notebooks (Workbench) | — | A | ⏳ Not tried yet | [G009-workbench-idle-shutdown.md](G009-workbench-idle-shutdown.md) |
| G010 | 3.1 | Developer environments (Cloud Workstations) | — | B | ⏳ Not tried yet | [G010-cloud-workstations-contractors.md](G010-cloud-workstations-contractors.md) |
| G011 | 2.1 | Compute Engine (VM Manager) | — | C | ⏳ Not tried yet | [G011-vm-manager-patch-deployment.md](G011-vm-manager-patch-deployment.md) |
| G012 | 3.1 | GKE (Autopilot Pod resource requests) | — | C | ⏳ Not tried yet | [G012-autopilot-resource-requests.md](G012-autopilot-resource-requests.md) |
| G013 | 2.4 | Infrastructure as Code (Helm) | — | C | ⏳ Not tried yet | [G013-helm-third-party-gke.md](G013-helm-third-party-gke.md) |
| G014 | 2.4 | Infrastructure as Code (Fabric FAST) | — | A | ⏳ Not tried yet | [G014-fabric-fast-landing-zone.md](G014-fabric-fast-landing-zone.md) |
| G015 | 2.4 | AI-assisted tooling (Application Design Center) | — | A | ⏳ Not tried yet | [G015-application-design-center.md](G015-application-design-center.md) |
| G016 | 2.4 | AI-assisted tooling (Gemini CLI) | — | C | ⏳ Not tried yet | [G016-gemini-cli-terminal-agent.md](G016-gemini-cli-terminal-agent.md) |
| G017 | 2.4 | AI-assisted tooling (Google Antigravity) | — | D | ⏳ Not tried yet | [G017-antigravity-agent-ide.md](G017-antigravity-agent-ide.md) |
| G018 | 3.4 | Monitoring (Managed Service for Prometheus) | — | A | ⏳ Not tried yet | [G018-managed-prometheus.md](G018-managed-prometheus.md) |
| G019 | 3.4 | Cloud SQL (Query Insights) | — | B | ⏳ Not tried yet | [G019-cloud-sql-query-insights.md](G019-cloud-sql-query-insights.md) |
| G020 | 3.4 | Cost optimization (Active Assist) | — | D | ⏳ Not tried yet | [G020-active-assist-idle-rightsizing.md](G020-active-assist-idle-rightsizing.md) |
| G021 | 4.1 | IAM (IAM recommender / Active Assist) | — | D | ⏳ Not tried yet | [G021-iam-recommender-excess-permissions.md](G021-iam-recommender-excess-permissions.md) |
| G022 | 3.4 | Monitoring (Cloud Hub) | — | C | ⏳ Not tried yet | [G022-cloud-hub-app-health.md](G022-cloud-hub-app-health.md) |
| G023 | 3.4 | Troubleshooting (Gemini Cloud Assist) | — | B | ⏳ Not tried yet | [G023-gemini-cloud-assist-investigation.md](G023-gemini-cloud-assist-investigation.md) |
| G024 | 3.4 | Monitoring (Gemini Cloud Assist for Cloud Monitoring) | — | D | ⏳ Not tried yet | [G024-gemini-promql-help.md](G024-gemini-promql-help.md) |
| G025 | 3.4 | Monitoring (Personalized Service Health) | — | D | ⏳ Not tried yet | [G025-personalized-service-health-alerts.md](G025-personalized-service-health-alerts.md) |
| G026 | 3.4 | Networking logs (VPC Flow Logs) | — | C | ⏳ Not tried yet | [G026-vpc-flow-logs.md](G026-vpc-flow-logs.md) |
| G027 | 3.4 | VPC firewall (Firewall Rules Logging) | — | B | ⏳ Not tried yet | [G027-firewall-rules-logging.md](G027-firewall-rules-logging.md) |
| G028 | 3.3 | VPC networking (custom static routes) | — | B | ⏳ Not tried yet | [G028-custom-static-route.md](G028-custom-static-route.md) |
| G029 | 2.3 | VPC firewall (Cloud NGFW FQDN objects) | — | A | ⏳ Not tried yet | [G029-ngfw-fqdn-egress.md](G029-ngfw-fqdn-egress.md) |
| G030 | 2.3 | VPC firewall (Cloud NGFW Enterprise IPS) | — | B | ⏳ Not tried yet | [G030-ngfw-enterprise-ips.md](G030-ngfw-enterprise-ips.md) |
| G031 | 2.3 | Hybrid networking (HA VPN) | — | A | ⏳ Not tried yet | [G031-ha-vpn-9999.md](G031-ha-vpn-9999.md) |
| G032 | 1.1 | Security (Cloud Asset Inventory feeds) | — | D | ⏳ Not tried yet | [G032-asset-inventory-feed.md](G032-asset-inventory-feed.md) |
| G033 | 1.1 | IAM (Cloud Asset Inventory IAM search) | — | A | ⏳ Not tried yet | [G033-asset-search-all-iam-policies.md](G033-asset-search-all-iam-policies.md) |
| G034 | 1.1 | Quotas (assess and request increases) | — | C | ⏳ Not tried yet | [G034-quota-increase-gpus.md](G034-quota-increase-gpus.md) |
| G035 | 1.1 | Compute Engine (regions and zones availability) | — | D | ⏳ Not tried yet | [G035-check-gpu-zone-availability.md](G035-check-gpu-zone-availability.md) |
| G036 | 3.1 | Compute Engine (attaching GPUs) | — | B | ⏳ Not tried yet | [G036-attach-gpu-maintenance-terminate.md](G036-attach-gpu-maintenance-terminate.md) |
| G037 | 2.1 | Serverless (Eventarc audit log triggers) | — | C | ⏳ Not tried yet | [G037-eventarc-audit-log-trigger.md](G037-eventarc-audit-log-trigger.md) |
| G038 | 2.1 | GKE (regional clusters) | — | B | ⏳ Not tried yet | [G038-gke-regional-cluster.md](G038-gke-regional-cluster.md) |
| G039 | 2.1 | GKE (kubectl install and authentication) | — | A | ⏳ Not tried yet | [G039-gke-gcloud-auth-plugin.md](G039-gke-gcloud-auth-plugin.md) |
| G040 | 3.1 | Cloud Run (revisions and tags) | — | B | ⏳ Not tried yet | [G040-cloud-run-no-traffic-tag.md](G040-cloud-run-no-traffic-tag.md) |
| G041 | 2.2 | Cloud SQL (cross-region DR) | — | B | ⏳ Not tried yet | [G041-cloud-sql-cross-region-replica.md](G041-cloud-sql-cross-region-replica.md) |
| G042 | 2.2 | Cloud Storage (dual-region, turbo replication) | — | D | ⏳ Not tried yet | [G042-dual-region-turbo-replication.md](G042-dual-region-turbo-replication.md) |
| G043 | 3.2 | Cloud Storage (Autoclass) | — | C | ⏳ Not tried yet | [G043-storage-autoclass.md](G043-storage-autoclass.md) |
| G044 | 3.2 | Firestore (backup and restore) | — | C | ⏳ Not tried yet | [G044-firestore-scheduled-backups.md](G044-firestore-scheduled-backups.md) |
| G045 | 3.2 | Databases (AlloyDB backup and restore) | — | A | ⏳ Not tried yet | [G045-alloydb-pitr-restore.md](G045-alloydb-pitr-restore.md) |
| G046 | 3.2 | Dataflow (reviewing job status) | — | D | ⏳ Not tried yet | [G046-dataflow-job-monitoring.md](G046-dataflow-job-monitoring.md) |
| G047 | 3.2 | BigQuery (executing queries) | — | B | ⏳ Not tried yet | [G047-bq-query-cli.md](G047-bq-query-cli.md) |
| G048 | 3.4 | Diagnostics (Cloud Profiler) | — | B | ⏳ Not tried yet | [G048-cloud-profiler.md](G048-cloud-profiler.md) |
| G049 | 3.1 | Cloud Run (autoscaling and concurrency) | — | B | ⏳ Not tried yet | [G049-cloud-run-concurrency.md](G049-cloud-run-concurrency.md) |
| G050 | 3.4 | Monitoring (uptime checks) | — | A | ⏳ Not tried yet | [G050-uptime-check-alert.md](G050-uptime-check-alert.md) |
