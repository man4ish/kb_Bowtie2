# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class ReadsAlignmentUtils(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='dev',  #IMPORTANT- switch to release once the utils are released!
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('ReadsAlignmentUtils', job_id)

    def _validate_alignment_submit(self, params, context=None):
        return self._client._submit_job(
             'ReadsAlignmentUtils.validate_alignment', [params],
             self._service_ver, context)

    def validate_alignment(self, params, context=None):
        """
        :param params: instance of type "ValidateAlignmentParams" (* Input
           parameters for validating a reads alignment *) -> structure:
           parameter "file_path" of String, parameter "ignore" of list of
           String
        :returns: instance of type "ValidateAlignmentOutput" (* Results from
           validate alignment *) -> structure: parameter "validated" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        """
        job_id = self._validate_alignment_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _upload_alignment_submit(self, params, context=None):
        return self._client._submit_job(
             'ReadsAlignmentUtils.upload_alignment', [params],
             self._service_ver, context)

    def upload_alignment(self, params, context=None):
        """
        Validates and uploads the reads alignment  *
        :param params: instance of type "UploadAlignmentParams" (* Required
           input parameters for uploading a reads alignment string
           destination_ref -  object reference of alignment destination. The
           object ref is 'ws_name_or_id/obj_name_or_id' where ws_name_or_id
           is the workspace name or id and obj_name_or_id is the object name
           or id file_path         -  Source: file with the path of the sam
           or bam file to be uploaded library_type      - ���single_end��� or
           ���paired_end��� condition         - genome_id         - 
           workspace id of genome annotation that was used to build the
           alignment read_sample_id    -  workspace id of read sample used to
           make the alignment file *) -> structure: parameter
           "destination_ref" of String, parameter "file_path" of String,
           parameter "library_type" of String, parameter "condition" of
           String, parameter "genome_id" of String, parameter
           "read_sample_id" of String, parameter "aligned_using" of String,
           parameter "aligner_version" of String, parameter "aligner_opts" of
           mapping from String to String, parameter "replicate_id" of String,
           parameter "platform" of String, parameter "bowtie2_index" of type
           "ws_bowtieIndex_id", parameter "sampleset_id" of type
           "ws_Sampleset_id", parameter "mapped_sample_id" of mapping from
           String to mapping from String to String, parameter "validate" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "ignore" of list of String
        :returns: instance of type "UploadAlignmentOutput" (*  Output from
           uploading a reads alignment  *) -> structure: parameter "obj_ref"
           of String
        """
        job_id = self._upload_alignment_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _download_alignment_submit(self, params, context=None):
        return self._client._submit_job(
             'ReadsAlignmentUtils.download_alignment', [params],
             self._service_ver, context)

    def download_alignment(self, params, context=None):
        """
        Downloads alignment files in .bam, .sam and .bai formats. Also downloads alignment stats *
        :param params: instance of type "DownloadAlignmentParams" (* Required
           input parameters for downloading a reads alignment string
           source_ref -  object reference of alignment source. The object ref
           is 'ws_name_or_id/obj_name_or_id' where ws_name_or_id is the
           workspace name or id and obj_name_or_id is the object name or id
           *) -> structure: parameter "source_ref" of String, parameter
           "downloadBAM" of type "boolean" (A boolean - 0 for false, 1 for
           true. @range (0, 1)), parameter "downloadSAM" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "downloadBAI" of type "boolean" (A boolean - 0 for false, 1 for
           true. @range (0, 1)), parameter "validate" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "ignore" of list of String
        :returns: instance of type "DownloadAlignmentOutput" (*  The output
           of the download method.  *) -> structure: parameter "ws_id" of
           String, parameter "bam_file" of String, parameter "sam_file" of
           String, parameter "bai_file" of String, parameter "stats" of type
           "AlignmentStats" (* @optional singletons multiple_alignments,
           properly_paired, alignment_rate, unmapped_reads, mapped_sections
           total_reads, mapped_reads *) -> structure: parameter
           "properly_paired" of Long, parameter "multiple_alignments" of
           Long, parameter "singletons" of Long, parameter "alignment_rate"
           of Double, parameter "unmapped_reads" of Long, parameter
           "mapped_reads" of Long, parameter "total_reads" of Long
        """
        job_id = self._download_alignment_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _export_alignment_submit(self, params, context=None):
        return self._client._submit_job(
             'ReadsAlignmentUtils.export_alignment', [params],
             self._service_ver, context)

    def export_alignment(self, params, context=None):
        """
        Wrapper function for use by in-narrative downloaders to download alignments from shock *
        :param params: instance of type "ExportParams" (* Required input
           parameters for exporting a reads alignment string source_ref - 
           object reference of alignment source. The object ref is
           'ws_name_or_id/obj_name_or_id' where ws_name_or_id is the
           workspace name or id and obj_name_or_id is the object name or id
           *) -> structure: parameter "source_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        job_id = self._export_alignment_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        job_id = self._client._submit_job('ReadsAlignmentUtils.status', 
            [], self._service_ver, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]
