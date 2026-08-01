# Verified Official Source Catalog v1

Status: planning baseline verified on 2026-08-01. Every source must be revalidated before production onboarding.

## Core source entries

| Domain | Provider | Dataset / service | Expected refresh | License | Primary use |
|---|---|---|---|---|---|
| Administrative boundaries | National Land Surveying and Mapping Center | Township/district code service and boundary datasets | Irregular | Taiwan Government Open Data License v1 | County/town lookup, boundary geometry |
| Population | Department of Household Registration | Household and population statistics API/files | Annual and dataset-specific | Taiwan Government Open Data License v1 | Ten-year population trends, sex/household analysis |
| Pollution sites | Environmental Management Administration, MOENV | Soil and groundwater pollution site basic data | Daily | Taiwan Government Open Data License v1 | Site names, status, pollutants, coordinates, parcel and dates |
| Pollution control announcements | Environmental Management Administration, MOENV | Soil and groundwater pollution control area announcement data | Monthly | Taiwan Government Open Data License v1 | Legal announcement records and control-area flags |
| Soil control areas | Environmental Management Administration, MOENV | Soil pollution control area boundary maps | Six-monthly | Taiwan Government Open Data License v1 | Polygon overlay and area analysis |
| Groundwater control areas | Environmental Management Administration, MOENV | Groundwater pollution control area boundary maps | Monthly | Taiwan Government Open Data License v1 | Polygon overlay and area analysis |
| Pollution statistics | Environmental Management Administration, MOENV | National pollution-site counts and areas | Annual | Taiwan Government Open Data License v1 | County-level trend summaries |
| Soil map | Ministry of Agriculture | Soil map, TWD97 | Irregular | Taiwan Government Open Data License v1 | Soil series and map overlay |
| Groundwater wells | Water Resources Agency | Existing groundwater observation-well locations | Irregular | Taiwan Government Open Data License v1 | Well locations and hydrogeologic context |

## Required metadata captured for every onboarded source

- publisher and responsible agency
- official dataset identifier
- landing page and machine-readable endpoint
- access method and authentication requirement
- license and reuse restrictions
- published update frequency
- observed update behavior
- source publication date
- retrieval timestamp
- checksum and immutable raw snapshot location
- spatial reference system
- geographic and temporal coverage
- field mapping and unit mapping
- quality checks and known limitations
- APA 7 citation template
- production approval status

## Production rule

A dataset is not considered production-ready until legal/license review, field mapping review, sample import validation and subject-matter review are all approved. Search-result summaries or manually copied values are never production data.