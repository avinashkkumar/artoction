-- Table: public.home_feedback

-- DROP TABLE IF EXISTS public.home_feedback;

CREATE TABLE IF NOT EXISTS public.home_feedback
(
    id bigint NOT NULL DEFAULT nextval('home_feedback_id_seq'::regclass),
    feedback text COLLATE pg_catalog."default" NOT NULL,
    user_id bigint NOT NULL,
    status character varying(12) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT home_feedback_pkey PRIMARY KEY (id),
    CONSTRAINT home_feedback_user_id_56f97b5a_fk_account_account_id FOREIGN KEY (user_id)
        REFERENCES public.account_account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.home_feedback
    OWNER to artoction;
-- Index: home_feedback_user_id_56f97b5a

-- DROP INDEX IF EXISTS public.home_feedback_user_id_56f97b5a;

CREATE INDEX IF NOT EXISTS home_feedback_user_id_56f97b5a
    ON public.home_feedback USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;