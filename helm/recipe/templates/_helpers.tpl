{{/*
Expand the name of the chart.
*/}}
{{- define "recipe.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "recipe.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "recipe.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "recipe.labels" -}}
helm.sh/chart: {{ include "recipe.chart" . }}
{{ include "recipe.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "recipe.appLabels" -}}
app: {{ include "recipe.name" . }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "recipe.selectorLabels" -}}
app.kubernetes.io/name: {{ include "recipe.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
version: {{ default .Chart.AppVersion .Values.AppVersion }}
{{ include "recipe.appLabels" . }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "recipe.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "recipe.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
